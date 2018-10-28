# -*- coding: utf-8 -*-

"""
    sheetfu.model
    ~~~~~~~~~~~~~

    Implement the sheetfu model (Spreadsheet > Sheet > Range).
    :copyright: © 2018 by Social Point Labs.
    :license: MIT, see LICENSE for more details.
"""


from sheetfu.helpers import convert_a1_to_coordinates, convert_coordinates_to_a1, rgb_to_hex, hex_to_rgb
from sheetfu.exceptions import SheetNameNoMatchError, SheetIdNoMatchError, NoDataRangeError, SizeNotMatchingException
from sheetfu.parsers import CellParsers


class Spreadsheet:
    """Spreadsheet object from which we can access its sheets.
    """

    def __init__(self, client, spreadsheet_id):     # only one of those is allowed to be None.
        """
        :param client: A SpreadsheetApp instance.
        :param spreadsheet_id: The spreadsheet ID
        """
        self.client = client
        self.id = spreadsheet_id
        self.sheets = self.get_sheets()
        self.batches = list()

    def __repr__(self):
        return '<Spreadsheet object {}>'.format(self.id)

    def get_sheet(self, name, sid):
        """
        Create a sheet object from sheet ID and sheet name
        :param name: The name of the sheet.
        :param sid: the sheet ID of the sheet.
        :return Sheet object
        """
        return Sheet(
            client=self.client,
            spreadsheet=self,
            name=name,
            sid=sid
        )

    def get_sheets(self):
        """
        Requests every sheets associated to spreadsheets
        :return List of sheets object
        """
        request = self.client.sheet_service.spreadsheets().get(spreadsheetId=self.id, includeGridData=False)
        response = request.execute()
        sheets = [
            self.get_sheet(sheet['properties']['title'], sheet['properties']['sheetId'])
            for sheet in response['sheets']
        ]
        return sheets

    def get_sheet_by_name(self, name):
        """
        Find sheet by name.
        :param name: name of the sheet we want to access.
        :return: Sheet object matching name.
        """
        for sheet in self.sheets:
            if sheet.name == name:
                return sheet
        else:
            raise SheetNameNoMatchError

    def get_sheet_by_id(self, sid):
        """
        Find sheet by sheet id.
        :param sid: id of the sheet we want to access.
        :return: Sheet object matching id.
        """
        for sheet in self.sheets:
            if sheet.sid == sid:
                return sheet
        else:
            raise SheetIdNoMatchError

    def commit(self):
        body = {'requests': [self.batches]}
        return self.client.sheet_service.spreadsheets().batchUpdate(
            spreadsheetId=self.id,
            body=body
        ).execute()


class Sheet:
    """Sheet object from which Range objects are accessible."""

    def __init__(self, client, spreadsheet, name, sid):
        """
        Instantiate
        :param client: The sheet client (SpreadsheetApp object).
        :param spreadsheet_id: The spreadsheet_id of the parent spreadsheet.
        :param name: Name/Title of the sheet (tab).
        :param sid: The sheet id.
        """
        self.client = client
        self.spreadsheet = spreadsheet
        self.name = name
        self.sid = sid
        self.batches = list()

    def __repr__(self):
        return '<Sheet object {}>'.format(self.name)

    def get_range(self, row, column, number_of_row=1, number_of_column=1):
        """
        Get a range object for given cells coordinates.
        :param row: Starting row of the target range (int)
        :param column: Starting column of the target range (int)
        :param number_of_row: Number of rows in the target range.
        :param number_of_column: Number of columns in the target range.
        :return: Range object.
        """
        a1 = convert_coordinates_to_a1(row, column, number_of_row, number_of_column)
        return Range(
            client=self.client,
            sheet=self,
            a1=a1,
        )

    def get_range_from_a1(self, a1_notification):
        """
        Get a Range object for a given A1 notation.
        :param a1_notification: The target A1 notation.
        :return: Range object.
        """
        return Range(
            client=self.client,
            sheet=self,
            a1=a1_notification,
        )

    def get_data_range(self):
        """
        Get the Range object for all the data contained in the sheet. Very useful when unsure about the size of the data
        in queried sheet.
        :return: Range Object.
        """
        return Range(
            client=self.client,
            sheet=self,
        )


def check_size(f):
    """
    Decorator to check length of the 2D matrix to be set. Raise an error if lengths are not matching with Range
    object coordinates.
    """
    def wrapper(range_object, data, batch_to=None):
        if len(data) != range_object.coordinates.number_of_rows:
            error_message = "Wrong number of rows. {} instead of {}".format(
                len(data),
                range_object.coordinates.number_of_rows
            )
            raise SizeNotMatchingException(error_message)

        for i, row in enumerate(data):
            if len(row) != range_object.coordinates.number_of_columns:
                context = {
                    "i": i,
                    "columns": len(row),
                    "expected": range_object.coordinates.number_of_columns
                }
                error_message = "Wrong number of column in row {i}. {columns} instead of {expected}".format(**context)
                raise SizeNotMatchingException(error_message)

        else:
            return f(range_object, data, batch_to)

    return wrapper


class Range:
    def __init__(self, client, sheet, a1=None):
        """
        Object to represent a range of cells in a sheet.
        :param client:
        :param sheet: parent Sheet object.
        :param a1:
        """
        self.client = client
        self.sheet = sheet
        self.a1 = self.persist_a1_data_range(a1)     # this checks the data range coordinates
        self.coordinates = convert_a1_to_coordinates(self.a1)

        # placeholder for putting requests object if we
        # want to send multiple set requests in one api call.
        self.batches = list()

    def __repr__(self):
        a1 = self.a1 or self.sheet.name
        return '<Range object {}>'.format(a1)

    def make_get_request(self, field_mask, cell_parser):
        """
        Make a get request for the range.
        :param field_mask: The targeted dimension (node, background, formula, ...).
        :param cell_parser: Function to run to parse cell data as expected.
        :return: The raw response of the request.
        """
        target_range = self.a1 or self.sheet.name
        # first we request data to the API
        request = self.client.sheet_service.spreadsheets().get(
            spreadsheetId=self.sheet.spreadsheet.id,
            includeGridData=True,
            ranges=[target_range],
            fields=field_mask
        )
        response = request.execute()
        # now we parse the rows from the response using the cell parser
        data = []
        values = response["sheets"][0]["data"]

        for row in range(0, self.coordinates.number_of_rows):
            data_row = []
            for column in range(0, self.coordinates.number_of_columns):
                try:
                    cell = values[0]["rowData"][row]["values"][column]
                    data_row.append(cell_parser(cell))

                except (KeyError, IndexError):
                    data_row.append("")

            data.append(data_row)
        return data

    def make_set_request(self, field, data, set_parser, batch_to=None):
        """
        Make a set request for the range.
        :param field: the targeted field.
        :param data: the 2D arrays with size matching range coordinates.
        :param set_parser: the function to run as a cell parser.
        :param batch_to: Object from which the request must be batched. Object must contain a 'batches' attribute.
        :return: raw response from the API.
        """
        # Parsing the rows to be in API format
        rows = []
        for row in data:
            row_data = {'values': []}
            for cell in row:
                row_data['values'].append(set_parser(cell))
            rows.append(row_data)

        # preparing the request
        request = {
            'updateCells': {
                'range': self.get_grid_range(),
                'fields': field,
                'rows': rows
            }
        }

        if batch_to is None:
            body = {'requests': [request]}
            return self.client.sheet_service.spreadsheets().batchUpdate(
                spreadsheetId=self.sheet.spreadsheet.id,
                body=body
            ).execute()

        return batch_to.batches.append(request)

    def get_values(self):
        data = self.make_get_request(
            field_mask="sheets/data/rowData/values/effectiveValue",
            cell_parser=CellParsers.get_value
        )
        return data

    @check_size
    def set_values(self, values, batch_to=None):
        """
        Set values for the Range.
        :param values: 2D array of values (size must match range coordinates).
        """
        return self.make_set_request(
            field='userEnteredValue',
            data=values,
            set_parser=CellParsers.set_value,
            batch_to=batch_to
        )

    def set_value(self, value, batch_to=None):
        values = list()
        for row in range(0, self.coordinates.number_of_rows):
            values.append(list())
            for column in range(0, self.coordinates.number_of_columns):
                values[row].append(value)

        return self.set_values(values, batch_to)

    def get_backgrounds(self):
        """
        Get the backgrounds of the Range.
        :return: 2D array of the background colors, of size matching the range coordinates.
        :return: 2D matrix of the colors in hex format.
        """
        return self.make_get_request(
            field_mask="sheets/data/rowData/values/effectiveFormat/backgroundColor",
            cell_parser=CellParsers.get_background
        )

    @check_size
    def set_backgrounds(self, backgrounds, batch_to=None):
        """
        Set color backgrounds for the Range.
        :param backgrounds: 2D array of notes (size must match range coordinates).
        """
        return self.make_set_request(
            field='userEnteredFormat.backgroundColor',
            data=backgrounds,
            set_parser=CellParsers.set_background,
            batch_to=batch_to
        )

    def set_background(self, background_color, batch_to=None):
        backgrounds = list()
        for row in range(0, self.coordinates.number_of_rows):
            backgrounds.append(list())
            for column in range(0, self.coordinates.number_of_columns):
                backgrounds[row].append(background_color)

        return self.set_backgrounds(backgrounds, batch_to)

    def get_notes(self):
        """
        Get the notes of the Range.
        :return: 2D array of the notes, of size matching the range coordinates.
        """
        return self.make_get_request(
            field_mask="sheets/data/rowData/values/note",
            cell_parser=CellParsers.get_note
        )

    @check_size
    def set_notes(self, notes, batch_to=None):
        """
        Set notes for the Range.
        :param notes: 2D array of notes (size must match range coordinates).
        """
        return self.make_set_request(
            field='note',
            data=notes,
            set_parser=CellParsers.set_note,
            batch_to=batch_to
        )

    def set_note(self, note, batch_to=None):
        notes = list()
        for row in range(0, self.coordinates.number_of_rows):
            notes.append(list())
            for column in range(0, self.coordinates.number_of_columns):
                notes[row].append(note)

        return self.set_values(notes, batch_to)

    def get_font_colors(self):
        """
        Get the font colors of the Range.
        :return: 2D array of the font colors, of size matching the range coordinates.
        """
        return self.make_get_request(
            field_mask="sheets/data/rowData/values/effectiveFormat/textFormat/foregroundColor",
            cell_parser=CellParsers.get_font_color
        )

    @check_size
    def set_font_colors(self, colors, batch_to=None):
        """
        Set font colors for the Range.
        :param colors: 2D array of font colors (size must match range coordinates).
        """
        return self.make_set_request(
            field='userEnteredFormat.textFormat.foregroundColor',
            data=colors,
            set_parser=CellParsers.set_font_color,
            batch_to=batch_to
        )

    def set_font_color(self, font_color, batch_to=None):
        font_colors = list()
        for row in range(0, self.coordinates.number_of_rows):
            font_colors.append(list())
            for column in range(0, self.coordinates.number_of_columns):
                font_colors[row].append(font_color)

        return self.set_font_colors(font_colors, batch_to)

    def get_formulas(self):
        """
        Get the formulas of the Range.
        :return: 2D array of the formulas strings, of size matching the range coordinates.
        """
        data = self.make_get_request(
            field_mask="sheets/data/rowData/values/userEnteredValue/formulaValue",
            cell_parser=CellParsers.get_formula
        )
        return data

    @check_size
    def set_formulas(self, formulas, batch_to=None):
        """
        Set formulas for the Range.
        :param formulas: 2D array of formulas (size must match range coordinates).
        """
        # todo: set formula.
        return formulas

    def persist_a1_data_range(self, a1):
        """
        If a1 attribute is None (typically when we get_data_range, it calculates the a1 notation and range coordinates
        based on the number of rows and columns found in the data.
        :param data: raw response of a request for values to google sheets API.
        """
        if a1 is not None:
            return a1

        request = self.client.sheet_service.spreadsheets().values().get(
            spreadsheetId=self.sheet.spreadsheet.id,
            range=self.sheet.name
        )

        response = request.execute()
        display_a1 = response["range"]
        first_cell_a1 = display_a1.split('!')[1].split(':')[0]

        if response.get("values") is None:
            raise NoDataRangeError('No data found in sheet "{}"'.format(self.sheet.name))

        number_of_rows = len(response["values"])
        number_of_columns = 0
        for row in response["values"]:
            if len(row) > number_of_columns:
                number_of_columns = len(row)

        first_cell_coordinates = convert_a1_to_coordinates(first_cell_a1)
        return convert_coordinates_to_a1(
            row=first_cell_coordinates.row,
            column=first_cell_coordinates.column,
            number_of_row=number_of_rows,
            number_of_column=number_of_columns
        )

    def get_cell(self, row, column):        # todo: have a custom error when row and/or column is 0
        row_number = self.coordinates.row + row - 1
        column_number = self.coordinates.column + column - 1
        a1 = convert_coordinates_to_a1(row_number, column_number)
        return Range(
            client=self.client,
            sheet=self.sheet,
            a1=a1
        )

    def add_dropdown(self, choices, strict=True, batch_to=None):
        values = [{"userEnteredValue": choice} for choice in choices]
        request = {
            "setDataValidation": {
                'range': self.get_grid_range(),
                "rule": {
                    "condition": {
                        "type": 'ONE_OF_LIST',
                        "values": values,
                    },
                    "showCustomUi": True,
                    "strict": strict
                }
            }
        }
        if batch_to is None:
            body = {'requests': [request]}
            return self.client.sheet_service.spreadsheets().batchUpdate(
                spreadsheetId=self.sheet.spreadsheet.id,
                body=body
            ).execute()

        return batch_to.batches.append(request)

    def get_grid_range(self):
        """
        As explained here: https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets#GridRange
        :return: the grid range for set requests.
        """
        return {
            "sheetId": self.sheet.sid,
            "startRowIndex": self.coordinates.row - 1,
            "endRowIndex": self.coordinates.row - 1 + self.coordinates.number_of_rows,
            "startColumnIndex": self.coordinates.column - 1,
            "endColumnIndex": self.coordinates.column - 1 + self.coordinates.number_of_columns
        }

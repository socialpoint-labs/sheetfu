
from sheetfu.helpers import convert_coordinates_to_a1
from sheetfu.model import Range
from sheetfu.modules.table_selector import TableSelector


class Table:

    def __init__(self, full_range, notes=False, backgrounds=False, font_colors=False, header_row=1):
        self.full_range = full_range.offset(
            row_offset=(header_row - 1),
            column_offset=0,
            num_rows=(full_range.coordinates.number_of_rows - (header_row - 1))
        ).trim_empty_bottom_rows()
        self.items_range = self.get_items_range()

        table_data = self.full_range.get_values()
        self.header = table_data[0]

        # Boolean values that represent if the Table contains this information #
        self.has_notes = notes
        self.has_backgrounds = backgrounds
        self.has_font_colors = font_colors

        self.items = self.parse_items(values=table_data[1:])

        self.batches = list()
        # This attribute determines if the next commit will re-write the whole table instead of executing the batches #
        self.needs_full_table_syncro = False

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    @staticmethod
    def get_table_from_sheet(spreadsheet, sheet_name, notes=False,
                             backgrounds=False, font_colors=False,
                             header_row=1):
        """
        Method to create a table from a whole sheet of a spreadsheet.
        This method assumes the header row is 1.

        :param spreadsheet: spreadsheet in which the table is in.
        :param sheet_name: specific sheet of the spreadsheet where the table is.
        :param notes: parameter to include the notes of a sheet.
        :param backgrounds: parameter to include the backgrounds of a sheet.
        :param font_colors: parameter to include the font colors of a sheet.
        :param header_row: parameter to specify in which row is the header of the table.

        :return: List of Items containing only filtered items or and empty List.

        """
        data_range = spreadsheet.get_sheet_by_name(sheet_name).get_data_range()
        return Table(data_range, notes, backgrounds, font_colors, header_row)


    def get_items_range(self):
        # We need to check for the case where the table has no items, only the header row #
        full_range_num_rows = self.full_range.coordinates.number_of_rows
        if full_range_num_rows == 1:
            return None
        return self.full_range.offset(row_offset=1, column_offset=0, num_rows=(full_range_num_rows - 1))

    def parse_items(self, values):
        items = list()
        if not self.items_range:
            return items

        empty_list = [None] * self.items_range.coordinates.number_of_rows

        notes = self.items_range.get_notes() if self.has_notes else list(empty_list)
        backgrounds = self.items_range.get_backgrounds() if self.has_backgrounds else list(empty_list)
        font_colors = self.items_range.get_font_colors() if self.has_font_colors else list(empty_list)

        for row_number in range(0, self.items_range.coordinates.number_of_rows):

            item = Item(
                parent_table=self,
                row_index=row_number,
                header=self.header,
                values=values[row_number],
                notes=notes[row_number],
                backgrounds=backgrounds[row_number],
                font_colors=font_colors[row_number]
            )
            items.append(item)
        return items

    def add_one(self, item_dict):
        values = [item_dict[label]for label in self.header]
        new_item = Item(
            parent_table=self,
            row_index=len(self.items),
            header=self.header,
            values=values,
            notes=[''] * len(self.header) if self.has_notes else None,
            backgrounds=[''] * len(self.header) if self.has_backgrounds else None,
            font_colors=[''] * len(self.header) if self.has_font_colors else None,
        )
        self.full_range = self.full_range.offset(
            row_offset=0,
            column_offset=0,
            num_rows=self.full_range.coordinates.number_of_rows + 1)
        self.items_range = self.get_items_range()
        self.items.append(new_item)
        new_item.get_range().set_values([values], batch_to=self)

    def sort(self, field, reverse=False):
        if not self.items_range:
            return
        self.items.sort(key=lambda item: item.get_field_value(field), reverse=reverse)
        self.needs_full_table_syncro = True

    def get_full_table_syncro_batches(self):
        self.batches = list()
        table_values, table_notes, table_backgrounds, table_font_colors = list(), list(), list(), list()
        for item in self.items:
            item_values, item_notes, item_backgrounds, item_font_colors = list(), list(), list(), list()
            for field_name in self.header:
                item_values.append(item.get_field_value(field_name))
                if self.has_notes:
                    item_notes.append(item.get_field_note(field_name))
                if self.has_backgrounds:
                    item_backgrounds.append(item.get_field_background(field_name))
                if self.has_font_colors:
                    item_font_colors.append(item.get_field_font_color(field_name))
            table_values.append(item_values)
            table_notes.append(item_notes)
            table_backgrounds.append(item_backgrounds)
            table_font_colors.append(item_font_colors)

        self.items_range.set_values(table_values, batch_to=self)
        if self.has_notes:
            self.items_range.set_notes(table_notes, batch_to=self)
        if self.has_backgrounds:
            self.items_range.set_backgrounds(table_backgrounds, batch_to=self)
        if self.has_font_colors:
            self.items_range.set_font_colors(table_font_colors, batch_to=self)

    def commit(self):
        if self.needs_full_table_syncro:
            self.get_full_table_syncro_batches()
            self.needs_full_table_syncro = False
        if len(self.batches) == 0:
            # Sending a batch update with an empty list of requests would return an error
            return
        body = {'requests': [self.batches]}
        response = self.full_range.client.sheet_service.spreadsheets().batchUpdate(
            spreadsheetId=self.full_range.sheet.spreadsheet.id,
            body=body
        ).execute()
        self.batches = list()
        return response

    def select(self, criteria):

        return TableSelector(self.items, criteria).execute()


class Item:

    def __init__(self, row_index, header, values, notes=None, backgrounds=None, font_colors=None, parent_table=None):
        self.row_index = row_index
        self.header = header
        self.values = values
        self.notes = notes
        self.backgrounds = backgrounds
        self.font_colors = font_colors

        # needed so we can commit things at table level easily
        self.table = parent_table

    def get_index(self, field_name):
        return self.header.index(field_name)

    def get_field_value(self, target_field):
        return self.values[self.get_index(target_field)]

    def get_field_note(self, target_field):
        if not self.table.has_notes:
            raise AttributeError("The table was not built reading the notes of the sheet.")
        return self.notes[self.get_index(target_field)]

    def get_field_background(self, target_field):
        if not self.table.has_backgrounds:
            raise AttributeError("The table was not built reading the backgrounds of the sheet.")
        return self.backgrounds[self.get_index(target_field)]

    def get_field_font_color(self, target_field):
        if not self.table.has_font_colors:
            raise AttributeError("The table was not built reading the font colors of the sheet.")
        return self.font_colors[self.get_index(target_field)]

    def get_range(self):
        a1 = convert_coordinates_to_a1(
            row= self.table.items_range.coordinates.row + self.row_index,
            column=self.table.items_range.coordinates.column,
            number_of_row=1,
            number_of_column=self.table.items_range.coordinates.number_of_columns,
            sheet_name=self.table.items_range.coordinates.sheet_name
        )
        return Range(
            client=self.table.full_range.client,
            sheet=self.table.full_range.sheet,
            a1=a1
        )

    def get_field_range(self, target_field):
        # rows and columns index start at 1
        # row will always be 1 in that case
        # as an item is contained in one row
        row = 1
        column = self.get_index(target_field) + 1
        return self.get_range().get_cell(row, column)

    def set_field_value(self, target_field, value):
        if self.values:
            self.values[self.get_index(target_field)] = value
        self.get_field_range(target_field).set_value(value, batch_to=self.table)

    def set_field_note(self, target_field, note):
        if self.notes:
            self.notes[self.get_index(target_field)] = note
        self.get_field_range(target_field).set_note(note, batch_to=self.table)

    def set_field_background(self, target_field, background_hex):
        if self.backgrounds:
            self.backgrounds[self.get_index(target_field)] = background_hex
        self.get_field_range(target_field).set_background(background_hex, batch_to=self.table)

    def set_field_font_color(self, target_field, font_color_hex):
        if self.font_colors:
            self.font_colors[self.get_index(target_field)] = font_color_hex
        self.get_field_range(target_field).set_font_color(font_color_hex, batch_to=self.table)

    def matches_value(self, header, value):
        item_value = self.get_field_value(header)
        return item_value == value

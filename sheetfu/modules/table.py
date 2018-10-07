from sheetfu.model import Range
from sheetfu.helpers import convert_coordinates_to_a1


class Table:

    def __init__(self, full_range, notes=False, backgrounds=False, font_colors=False):
        self.full_range = full_range

        self.values = self.full_range.get_values()
        self.notes = self.full_range.get_notes() if notes else None
        self.backgrounds = self.full_range.get_backgrounds() if backgrounds else None
        self.font_colors = self.full_range.get_font_colors() if font_colors else None

        self.header = self.values[0]
        self.items_range = self.get_items_range()

        self.items = self.parse_items()

        self.batches = list()

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def get_items_range(self):
        a1 = convert_coordinates_to_a1(
            row=self.full_range.coordinates.row + 1,
            column=self.full_range.coordinates.column,
            number_of_row=self.full_range.coordinates.number_of_rows - 1,
            number_of_column=self.full_range.coordinates.number_of_columns
        )
        return Range(
            client=self.full_range.client,
            sheet=self.full_range.sheet,
            a1=a1
        )

    def parse_items(self):
        items = list()
        for row_number in range(0, self.items_range.coordinates.number_of_rows):
            values = self.values[row_number] or None
            notes = self.notes[row_number] or None
            backgrounds = self.backgrounds[row_number] or None
            font_colors = self.font_colors[row_number] or None
            item = Item(
                parent_table=self,
                row_index=row_number,
                header=self.header,
                values=values,
                notes=notes,
                backgrounds=backgrounds,
                font_colors=font_colors
            )
            items.append(item)
        return items

    def commit(self):
        body = {'requests': [self.batches]}
        return self.full_range.client.sheet_service.spreadsheets().batchUpdate(
            spreadsheetId=self.full_range.spreadsheet.id,
            body=body
        ).execute()


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
        return self.notes[self.get_index(target_field)]

    def get_field_background(self, target_field):
        return self.backgrounds[self.get_index(target_field)]

    def get_field_font_color(self, target_field):
        return self.font_colors[self.get_index(target_field)]

    def get_range(self):
        a1 = convert_coordinates_to_a1(
            row= self.table.items_range.coordinates.row + self.row_index,
            column=self.table.items_range.coordinates.column,
            number_of_row=1,
            number_of_column=self.table.items_range.coordinates.number_of_columns
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

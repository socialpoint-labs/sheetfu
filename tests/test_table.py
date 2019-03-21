from sheetfu import Table
from sheetfu.modules.table import Item
from tests.utils import mock_google_sheets_responses
from sheetfu import SpreadsheetApp
from sheetfu.model import Range


class TestTableRanges:

    http_mocks = mock_google_sheets_responses([
        'table_get_sheets.json',
        'table_check_data_range.json',
        'table_values.json',
        'table_values.json',
        'table_notes.json',
        'table_backgrounds.json',
        'table_font_colors.json'
    ])

    sa = SpreadsheetApp(http=http_mocks)
    table_range = sa.open_by_id('whatever').get_sheet_by_name('Sheet1').get_data_range()
    table = Table(
        full_range=table_range,
        notes=True,
        backgrounds=True,
        font_colors=True
    )

    def test_full_range_data(self):
        for item in self.table.items:
            assert item.backgrounds is not None
            assert item.notes is not None
            assert item.font_colors is not None
            assert item.values is not None
            assert len(item.header) == len(self.table.header)

    def test_items(self):
        assert self.table.items is not None
        assert type(self.table.items) == list
        assert len(self.table.items) == self.table.full_range.coordinates.number_of_rows - 1

    def test_items_instance(self):
        for item in self.table.items:
            assert isinstance(item, Item)
            assert isinstance(item.get_range(), Range)

    def test_table_length(self):
        assert len(self.table) == len(self.table.items)

    def test_for_loops(self):
        for item in self.table:
            assert isinstance(item, Item)


class TestItem:
    http_mocks = mock_google_sheets_responses([
        'table_get_sheets.json',
        'table_check_data_range.json',
        'table_values.json',
        'table_values.json',
        'table_notes.json',
        'table_backgrounds.json',
        'table_font_colors.json'
    ])
    sa = SpreadsheetApp(http=http_mocks)
    table_range = sa.open_by_id('whatever').get_sheet_by_name('Sheet1').get_data_range()
    table = Table(
        full_range=table_range,
        notes=True,
        backgrounds=True,
        font_colors=True
    )
    item = Item(
        parent_table=table,
        row_index=0,
        header=['name', 'surname'],
        values=['john', 'doe'],
        notes=['note name', 'note surname'],
        backgrounds=['#ffffff', '#fff000'],
        font_colors=['#000fff', '#000000']
    )

    def test_get_field_value(self):
        assert self.item.get_field_value('name') == 'john'
        assert self.item.get_field_value('surname') == 'doe'

    def test_get_field_note(self):
        assert self.item.get_field_note('name') == 'note name'
        assert self.item.get_field_note('surname') == 'note surname'

    def test_get_field_background(self):
        assert self.item.get_field_background('name') == '#ffffff'
        assert self.item.get_field_background('surname') == '#fff000'

    def test_get_field_font_colors(self):
        assert self.item.get_field_font_color('name') == '#000fff'
        assert self.item.get_field_font_color('surname') == '#000000'


class TestTableItemRanges:
    http_mocks = mock_google_sheets_responses([
        'table_get_sheets.json',
        'table_check_data_range.json',
        'table_values.json',
        'table_values.json',
        'table_notes.json',
        'table_backgrounds.json',
        'table_font_colors.json'
    ])

    sa = SpreadsheetApp(http=http_mocks)
    table_range = sa.open_by_id('whatever').get_sheet_by_name('Sheet1').get_data_range()
    table = Table(
        full_range=table_range,
        notes=True,
        backgrounds=True,
        font_colors=True
    )

    def test_table_range(self):
        assert self.table.full_range.a1 == 'Sheet1!A1:C6'

    def test_table_items_range(self):
        assert self.table.items_range.a1 == 'Sheet1!A2:C6'

    def test_first_item_range(self):
        first_item = self.table[0]
        assert isinstance(first_item, Item)
        assert first_item.get_range().a1 == 'Sheet1!A2:C2'

    def test_field_ranges_type(self):
        second_item = self.table[1]
        assert isinstance(second_item, Item)
        assert second_item.get_range().a1 == 'Sheet1!A3:C3'

        for field in ['name', 'surname', 'age']:
            field_range = second_item.get_field_range(field)
            assert isinstance(field_range, Range)

    def test_field_ranges(self):
        third_item = self.table[2]
        assert third_item.get_field_range('name').a1 == 'Sheet1!A4'
        assert third_item.get_field_range('surname').a1 == 'Sheet1!B4'
        assert third_item.get_field_range('age').a1 == 'Sheet1!C4'


class TestTableCRUD:
    http_mocks = mock_google_sheets_responses([
        'table_get_sheets.json',
        'table_check_data_range.json',
        'table_values.json',
        'table_values.json',
        'table_commit_reply.json',
        'table_commit_reply.json',
        'table_commit_reply.json',
    ])

    sa = SpreadsheetApp(http=http_mocks)
    table_range = sa.open_by_id('whatever').get_sheet_by_name('Sheet1').get_data_range()
    table = Table(
        full_range=table_range,
        notes=False,
        backgrounds=False,
        font_colors=False
    )

    def test_add_one_item(self):
        assert self.table.full_range.a1 == "Sheet1!A1:C6"
        assert self.table.items_range.a1 == "Sheet1!A2:C6"
        assert len(self.table.items) == 5
        self.table.add_one({"name": "Alex", "surname": "Muelas", "age": 1})
        assert self.table.full_range.a1 == "Sheet1!A1:C7"
        assert self.table.items_range.a1 == "Sheet1!A2:C7"
        assert len(self.table.batches) == 1
        assert len(self.table.items) == 6
        self.table.commit()
        assert len(self.table.batches) == 0
        assert len(self.table.items) == 6

    def test_add_several_items(self):
        assert len(self.table.items) == 6
        assert self.table.full_range.a1 == "Sheet1!A1:C7"
        assert self.table.items_range.a1 == "Sheet1!A2:C7"
        self.table.add_one({"name": "John", "surname": "Snpw", "age": 2})
        self.table.add_one({"name": "Ned", "surname": "Stark", "age": 3})
        self.table.add_one({"name": "Tyrion", "surname": "Lannister", "age": 4})
        assert len(self.table.batches) == 3
        assert len(self.table.items) == 9
        self.table.commit()
        assert len(self.table.batches) == 0
        assert len(self.table.items) == 9
        assert self.table.full_range.a1 == "Sheet1!A1:C10"
        assert self.table.items_range.a1 == "Sheet1!A2:C10"

    def test_sort_table(self):
        assert len(self.table.items) == 9
        self.table.sort("age")
        assert len(self.table.items) == 9
        assert self.table.items[0].get_field_value("name") == "Alex"
        assert self.table.items[8].get_field_value("name") == "philippe"
        assert self.table.needs_full_table_syncro == True



from sheetfu import Table
from sheetfu.modules.table import Item
from tests.utils import mock_google_sheets_responses
from sheetfu import SpreadsheetApp


class TestTableRanges:

    http_mocks = mock_google_sheets_responses([
        'table_get_sheets.json',
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
        assert self.table.backgrounds is not None
        assert self.table.notes is not None
        assert self.table.font_colors is not None
        assert self.table.values is not None

    def test_data_length(self):
        assert len(self.table.backgrounds) == len(self.table.notes) \
               == len(self.table.font_colors) == len(self.table.values)

    def test_items(self):
        assert self.table.items is not None
        assert type(self.table.items) == list
        assert len(self.table.items) == len(self.table.values) - 1

    def test_items_instance(self):
        for item in self.table.items:
            assert isinstance(item, Item)

    def test_table_length(self):
        assert len(self.table) == len(self.table.items)

    def test_for_loops(self):
        for item in self.table:
            assert isinstance(item, Item)


class TestItem:

    item = Item(
        parent_table=None,
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

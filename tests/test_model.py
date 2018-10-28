from sheetfu.client import SpreadsheetApp
from sheetfu.model import Spreadsheet, Sheet, Range
from tests.utils import mock_range_instance, mock_spreadsheet_instance, mock_google_sheets_responses


class TestModelClients:

    http_sheets_mocks = mock_range_instance()

    client = SpreadsheetApp(http=http_sheets_mocks)
    spreadsheet = client.open_by_id('some_id')
    sheet = spreadsheet.get_sheet_by_name("people")
    my_range = sheet.get_range(1, 1)

    def test_instances(self):
        assert isinstance(self.client, SpreadsheetApp)
        assert isinstance(self.spreadsheet, Spreadsheet)
        assert isinstance(self.sheet, Sheet)
        assert isinstance(self.my_range, Range)

    def test_client_is_in_every_object(self):
        assert self.client is self.spreadsheet.client
        assert self.client is self.sheet.client
        assert self.client is self.my_range.client


class TestSpreadsheet:

    http_sheets_mocks = mock_spreadsheet_instance()
    spreadsheet = SpreadsheetApp(http=http_sheets_mocks).open_by_id('some_id')

    def test_get_sheets(self):
        sheets = self.spreadsheet.sheets
        assert len(sheets) == 2
        for sheet in sheets:
            assert isinstance(sheet, Sheet)


class TestGettersFromDataRange:

    fixtures = ['get_backgrounds.json', 'get_notes.json', 'get_fonts.json']
    http_sheets_mocks = mock_range_instance(fixtures)
    client = SpreadsheetApp(http=http_sheets_mocks)
    data_range = client.open_by_id('spreadsheet id').get_sheet_by_name('people').get_data_range()

    def test_a1_notation_is_right(self):
        assert self.data_range.a1 == "A1:D21"

    def test_get_backgrounds(self):
        backgrounds = self.data_range.get_backgrounds()
        assert type(backgrounds) == list
        assert len(backgrounds) == self.data_range.coordinates.number_of_rows
        for row in backgrounds:
            assert len(row) == self.data_range.coordinates.number_of_columns


class TestCellRange:

    http_sheets_mocks = mock_range_instance()
    client = SpreadsheetApp(http=http_sheets_mocks)
    data_range = client.open_by_id('spreadsheet id').get_sheet_by_name('people').get_data_range()

    def test_a1(self):
        assert self.data_range.a1 == 'A1:D21'

    def test_get_cell(self):
        assert self.data_range.get_cell(1, 1).a1 == 'A1'
        assert self.data_range.get_cell(1, 2).a1 == 'B1'
        assert self.data_range.get_cell(2, 1).a1 == 'A2'


class TestGridRange:

    http_sheets_mocks = mock_spreadsheet_instance()
    spreadsheet = SpreadsheetApp(http=http_sheets_mocks).open_by_id('some_id')
    sheet = spreadsheet.sheets[0]

    def test_grid_range_one_cell(self):
        cell = self.sheet.get_range_from_a1('A1')
        assert cell.a1 == 'A1'
        cell_grid_range = cell.get_grid_range()
        assert cell_grid_range['startRowIndex'] == 0
        assert cell_grid_range['endRowIndex'] == 1
        assert cell_grid_range['startColumnIndex'] == 0
        assert cell_grid_range['endColumnIndex'] == 1

    def test_grid_range_multiple_cells(self):
        range_ = self.sheet.get_range_from_a1('A3:B4')
        assert range_.a1 == 'A3:B4'
        grid_range = range_.get_grid_range()
        assert grid_range['startRowIndex'] == 2
        assert grid_range['endRowIndex'] == 4
        assert grid_range['startColumnIndex'] == 0
        assert grid_range['endColumnIndex'] == 2


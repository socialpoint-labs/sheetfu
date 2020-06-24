from sheetfu.client import SpreadsheetApp
from sheetfu.exceptions import RowOrColumnEqualsZeroError
from sheetfu.model import Spreadsheet, Sheet, Range
from tests.utils import mock_range_instance, mock_spreadsheet_instance, mock_google_sheets_responses
from tests.utils import open_fixture
import pytest
import json


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

    http_sheets_mocks = mock_spreadsheet_instance(["add_sheets.json", "duplicate_sheets.json"])
    spreadsheet = SpreadsheetApp(http=http_sheets_mocks).open_by_id('some_id')

    def test_get_sheets(self):
        sheets = self.spreadsheet.sheets
        assert len(sheets) == 2
        for sheet in sheets:
            assert isinstance(sheet, Sheet)

    def test_create_sheets(self):
        self.spreadsheet.create_sheets(["test_sheet", "test_sheet_2"])
        assert len(self.spreadsheet.sheets) == 4

    def test_duplicate_sheet(self):
        # Important! This test needs to be executed after test_create_sheets, as it clones that sheet #
        self.spreadsheet.duplicate_sheet(new_sheet_name="cloned_sheet", sheet_name="test_sheet")
        assert len(self.spreadsheet.sheets) == 5

    def test_add_sheets_from_response(self):
        dummy_response_create = json.loads(open_fixture("add_sheets.json"))
        self.spreadsheet._add_sheets_from_response(response=dummy_response_create, reply_type="addSheet")
        assert len(self.spreadsheet.sheets) == 7
        dummy_response_duplicate = json.loads(open_fixture("duplicate_sheets.json"))
        self.spreadsheet._add_sheets_from_response(response=dummy_response_duplicate, reply_type="duplicateSheet")
        assert len(self.spreadsheet.sheets) == 8


class TestSheet:
    http_sheets_mocks = mock_range_instance()
    sheet = SpreadsheetApp(http=http_sheets_mocks).open_by_id("some_id").get_sheet_by_name("people")

    def test_sheet_properties(self):
        assert self.sheet.name == "people"
        assert self.sheet.sid == 0
        assert type(self.sheet.grid_properties) == dict
        assert type(self.sheet.batches) == list
        assert len(self.sheet.batches) == 0

    def test_max_rows_columns(self):
        assert self.sheet.get_max_rows() == 1000
        assert self.sheet.get_max_columns() == 26


class TestGettersFromDataRange:

    fixtures = ['get_backgrounds.json', 'get_notes.json', 'get_fonts.json']
    http_sheets_mocks = mock_range_instance(fixtures)
    client = SpreadsheetApp(http=http_sheets_mocks)
    data_range = client.open_by_id('spreadsheet id').get_sheet_by_name('people').get_data_range()

    def test_a1_notation_is_right(self):
        assert self.data_range.a1 == "people!A1:D21"

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
        assert self.data_range.a1 == 'people!A1:D21'

    def test_get_cell(self):
        assert self.data_range.get_cell(1, 1).a1 == 'people!A1'
        assert self.data_range.get_cell(1, 2).a1 == 'people!B1'
        assert self.data_range.get_cell(2, 1).a1 == 'people!A2'


class TestGridRange:

    http_sheets_mocks = mock_spreadsheet_instance()
    spreadsheet = SpreadsheetApp(http=http_sheets_mocks).open_by_id('some_id')
    sheet = spreadsheet.sheets[0]

    def test_grid_range_one_cell(self):
        cell = self.sheet.get_range_from_a1('A1')
        assert cell.a1 == 'people!A1'
        cell_grid_range = cell.get_grid_range()
        assert cell_grid_range['startRowIndex'] == 0
        assert cell_grid_range['endRowIndex'] == 1
        assert cell_grid_range['startColumnIndex'] == 0
        assert cell_grid_range['endColumnIndex'] == 1

    def test_grid_range_multiple_cells(self):
        range_ = self.sheet.get_range_from_a1('A3:B4')
        assert range_.a1 == 'people!A3:B4'
        grid_range = range_.get_grid_range()
        assert grid_range['startRowIndex'] == 2
        assert grid_range['endRowIndex'] == 4
        assert grid_range['startColumnIndex'] == 0
        assert grid_range['endColumnIndex'] == 2

    def test_offsets(self):
        range = self.sheet.get_range_from_a1('C5:E20')
        assert range.coordinates.row == 5
        assert range.coordinates.column == 3
        assert range.coordinates.number_of_rows == 16
        assert range.coordinates.number_of_columns == 3

        bottom_offset = range.offset(row_offset=5, column_offset=5)
        assert bottom_offset.coordinates.row == 10
        assert bottom_offset.coordinates.column == 8
        assert bottom_offset.coordinates.number_of_rows == 16
        assert bottom_offset.coordinates.number_of_columns == 3
        assert bottom_offset.a1 == "people!H10:J25"

        top_offset = range.offset(row_offset=-3, column_offset=-2)
        assert top_offset.coordinates.row == 2
        assert top_offset.coordinates.column == 1
        assert top_offset.coordinates.number_of_rows == 16
        assert top_offset.coordinates.number_of_columns == 3
        assert top_offset.a1 == "people!A2:C17"

    def test_offset_trims(self):
        range = self.sheet.get_range_from_a1('B1:D20')
        assert range.coordinates.row == 1
        assert range.coordinates.column == 2
        assert range.coordinates.number_of_rows == 20
        assert range.coordinates.number_of_columns == 3

        top_trimmed_range = range.offset(row_offset=2, column_offset=0, num_rows=18, num_columns=3)
        assert top_trimmed_range.coordinates.row == 3
        assert top_trimmed_range.coordinates.column == 2
        assert top_trimmed_range.coordinates.number_of_rows == 18
        assert top_trimmed_range.coordinates.number_of_columns == 3
        assert top_trimmed_range.a1 == "people!B3:D20"

        bottom_trimmed_range = range.offset(row_offset=0, column_offset=0, num_rows=15, num_columns=2)
        assert bottom_trimmed_range.coordinates.row == 1
        assert bottom_trimmed_range.coordinates.column == 2
        assert bottom_trimmed_range.coordinates.number_of_rows == 15
        assert bottom_trimmed_range.coordinates.number_of_columns == 2
        assert bottom_trimmed_range.a1 == "people!B1:C15"

        sides_trimmed_range = range.offset(row_offset=0, column_offset=1,
                                           num_rows=range.coordinates.number_of_rows, num_columns=1)
        assert sides_trimmed_range.coordinates.row == 1
        assert sides_trimmed_range.coordinates.column == 3
        assert sides_trimmed_range.coordinates.number_of_rows == 20
        assert sides_trimmed_range.coordinates.number_of_columns == 1
        assert sides_trimmed_range.a1 == "people!C1:C20"

    def test_invalid_offset_ranges(self):
        range = self.sheet.get_range_from_a1('A5:B10')
        assert range.coordinates.row == 5
        assert range.coordinates.column == 1
        assert range.coordinates.number_of_rows == 6
        assert range.coordinates.number_of_columns == 2
        with pytest.raises(ValueError):
            range.offset(row_offset=-5, column_offset=0)
        with pytest.raises(ValueError):
            range.offset(row_offset=0, column_offset=-1)
        with pytest.raises(ValueError):
            range.offset(row_offset=0, column_offset=0,
                         num_rows=0, num_columns=2)
        with pytest.raises(ValueError):
            range.offset(row_offset=0, column_offset=0,
                         num_rows=6, num_columns=-2)


class TestRangeMaxRowColumn:

    http_sheets_mocks = mock_spreadsheet_instance()
    spreadsheet = SpreadsheetApp(http=http_sheets_mocks).open_by_id('some_id')
    sheet = spreadsheet.sheets[0]

    def test_max_coordinates_a1(self):
        cell = self.sheet.get_range_from_a1('A1')
        assert cell.get_row() == 1
        assert cell.get_column() == 1
        assert cell.get_max_row() == 1
        assert cell.get_max_column() == 1

    def test_max_coordinates_a1_b4(self):
        range_ = self.sheet.get_range_from_a1('A1:B4')
        assert range_.get_row() == 1
        assert range_.get_column() == 1
        assert range_.get_max_row() == 4
        assert range_.get_max_column() == 2

    def test_max_coordinates_a3_b4(self):
        range_ = self.sheet.get_range_from_a1('B3:D4')
        assert range_.get_row() == 3
        assert range_.get_column() == 2
        assert range_.get_max_row() == 4
        assert range_.get_max_column() == 4


class TestSheetCreationMethodReturns:

    http_sheets_mocks = mock_spreadsheet_instance(["add_sheets.json", "duplicate_sheets.json"])
    spreadsheet = SpreadsheetApp(http=http_sheets_mocks).open_by_id('some_id')

    def test_create_sheets_types(self):
        new_sheets = self.spreadsheet.create_sheets(["test_sheet", "test_sheet_2"])
        assert isinstance(new_sheets, list)
        assert isinstance(new_sheets[0], Sheet)
        assert new_sheets[0].name == 'test_sheet'
        assert isinstance(new_sheets[1], Sheet)
        assert new_sheets[1].name == 'test_sheet_2'

    def test_duplicate_sheet_type(self):
        # Important! This test needs to be executed after test_create_sheets, as it clones that sheet #
        duplicated_sheet = self.spreadsheet.duplicate_sheet(new_sheet_name="cloned_sheet", sheet_name="test_sheet")
        assert isinstance(duplicated_sheet, Sheet)
        assert duplicated_sheet.name == 'cloned_sheet'


class TestWrongRowAndColumnValues:
    http_sheets_mocks = mock_range_instance()

    client = SpreadsheetApp(http=http_sheets_mocks)
    spreadsheet = client.open_by_id('some_id')
    sheet = spreadsheet.get_sheet_by_name("people")

    def test_invalid_row(self):
        with pytest.raises(RowOrColumnEqualsZeroError):
            self.sheet.get_range(row=0, column=1)

    def test_invalid_column(self):
        with pytest.raises(RowOrColumnEqualsZeroError):
            self.sheet.get_range(row=1, column=0)

    def test_invalid_row_and_column(self):
        with pytest.raises(RowOrColumnEqualsZeroError):
            self.sheet.get_range(row=0, column=0)


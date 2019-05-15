from sheetfu import SpreadsheetApp
from sheetfu.model import Spreadsheet, Sheet, Range
from tests.utils import mock_google_sheets_responses, mock_spreadsheet_instance, mock_range_instance
import os


class TestSpreadsheetApp:

    http_sheets_mocks = mock_google_sheets_responses(['create.json', 'get_sheets.json'])
    client = SpreadsheetApp(http=http_sheets_mocks)

    def test_client(self):
        assert self.client.sheet_service is not None

    def test_create_spreadsheet(self):
        spreadsheet = self.client.create("test_spreadsheet")
        assert isinstance(spreadsheet, Spreadsheet)


class TestSpreadsheetAppInstances:

    http_sheets_mocks = mock_spreadsheet_instance()
    client = SpreadsheetApp(http=http_sheets_mocks)
    spreadsheet = client.open_by_id(spreadsheet_id='')

    def test_spreadsheet_instance(self):
        assert isinstance(self.spreadsheet, Spreadsheet)

    def test_sheet_instance(self):
        sheet = self.spreadsheet.get_sheet_by_name('people')
        assert isinstance(sheet, Sheet)


class TestModelInstantiations:

    def test_one_line_spreadsheet_instance(self):
        http_sheets_mocks = mock_spreadsheet_instance()
        spreadsheet = SpreadsheetApp(http=http_sheets_mocks).open_by_id('some_id')
        assert isinstance(spreadsheet, Spreadsheet)

    def test_one_line_sheet_instance(self):
        http_sheets_mocks = mock_spreadsheet_instance()
        sheet = SpreadsheetApp(http=http_sheets_mocks).open_by_id('some_id').get_sheet_by_name('people')
        assert isinstance(sheet, Sheet)

    def test_one_line_sheet_instance_different_case(self):
        http_sheets_mocks = mock_spreadsheet_instance()
        sheet = SpreadsheetApp(http=http_sheets_mocks).open_by_id('some_id').get_sheet_by_name('PeOpLe')
        assert isinstance(sheet, Sheet)

    def test_one_line_range_instance(self):
        http_sheets_mocks = mock_spreadsheet_instance()
        sheet = SpreadsheetApp(http=http_sheets_mocks).open_by_id('some_id').get_sheet_by_name('people')
        sheet_range = sheet.get_range(row=1, column=1)
        assert isinstance(sheet_range, Range)


class TestOpenByUrl:

    secret_path = os.path.join(os.path.dirname(__file__), 'fake_secret.json')
    sheet_url = "https://docs.google.com/spreadsheets/d/10egVLKcTR0AQuQdZKp-MgGgErUdzDI_nnZHAWTfXK3I/edit#gid=1883950"

    def test_open_by_url(self):
        http_sheets_mocks = mock_spreadsheet_instance()
        spreadsheet = SpreadsheetApp(http=http_sheets_mocks).open_by_url(self.sheet_url)
        assert isinstance(spreadsheet, Spreadsheet)
        assert spreadsheet.id == "10egVLKcTR0AQuQdZKp-MgGgErUdzDI_nnZHAWTfXK3I"

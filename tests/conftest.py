import pytest

from sheetfu import SpreadsheetApp, Table
from tests.utils import mock_google_sheets_responses


@pytest.fixture()
def full_spreadsheet():
    http_mocks = mock_google_sheets_responses([
        'table_get_sheets.json',
        'table_check_data_range.json',
        'table_values.json',
        'table_values.json',
        'table_notes.json',
        'table_backgrounds.json',
        'table_font_colors.json'
    ])

    return SpreadsheetApp(http=http_mocks)


@pytest.fixture()
def spreadsheet():
    http_mocks = mock_google_sheets_responses([
        'table_get_sheets.json',
        'table_check_data_range.json',
        'table_values.json',
        'table_values.json',
        'table_commit_reply.json',
        'table_commit_reply.json',
        'table_commit_reply.json',
    ])

    return SpreadsheetApp(http=http_mocks)


@pytest.fixture()
def table(spreadsheet):
    table_range = spreadsheet.open_by_id('whatever').get_sheet_by_name('Sheet1').get_data_range()
    return Table(
        full_range=table_range,
        notes=False,
        backgrounds=False,
        font_colors=False
    )


@pytest.fixture()
def full_table(full_spreadsheet):
    table_range = full_spreadsheet.open_by_id('whatever').get_sheet_by_name('Sheet1').get_data_range()
    return Table(
        full_range=table_range,
        notes=True,
        backgrounds=True,
        font_colors=True
    )

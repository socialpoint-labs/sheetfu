import os
from googleapiclient.http import HttpMockSequence
from sheetfu.client import SpreadsheetApp
import json


def mock_google_sheets_responses(fixture_files=None):
    """
    Function to mock one or multiple requests to sheets.
    :param fixture_files: Fixture file name (must be located in the fixture folder).
    :return: An HttpMockSequence object.
    """
    mocks = [({'status': '200'}, open_fixture('discovery.json'))]

    # If input is a string, transform it into list of one item
    if isinstance(fixture_files, str):
        fixture_files = [fixture_files]

    # Add each fixture as a request mock if any
    if fixture_files:
        for file in fixture_files:
            mocks.append(({'status': '200'}, open_fixture(file)))
    http_mocks = HttpMockSequence(mocks)
    return http_mocks


def mock_spreadsheet_instance(fixtures=None):
    if fixtures is None:
        fixtures = []
    return mock_google_sheets_responses(['get_sheets.json'] + fixtures)


def mock_range_instance(fixtures=None):
    if fixtures is None:
        fixtures = []
    return mock_google_sheets_responses(['get_sheets.json', 'people.json'] + fixtures)


def open_fixture(fixture_filename):
    fixture_folder_path = os.path.join(os.path.dirname(__file__), "fixtures/")
    return open(fixture_folder_path + fixture_filename, "r").read()


def create_fixture(path_to_secret, spreadsheet_id, target_range, field_mask, fixture_name):
    client = SpreadsheetApp(path_to_secret)
    request = client.sheet_service.spreadsheets().get(
        spreadsheetId=spreadsheet_id,
        includeGridData=True,
        ranges=[target_range],
        fields=field_mask
    )
    folder = os.path.join(os.path.dirname(__file__), 'fixtures')
    response = request.execute()
    with open(os.path.join(folder, fixture_name), 'w') as f:
        content = json.dumps(response)
        f.write(content)


def create_values_fixture(path_to_secret, spreadsheet_id, target_range, fixture_name):
    client = SpreadsheetApp(path_to_secret)
    request = client.sheet_service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=target_range
    )
    folder = os.path.join(os.path.dirname(__file__), 'fixtures')
    response = request.execute()
    with open(os.path.join(folder, fixture_name), 'w') as f:
        content = json.dumps(response)
        f.write(content)

import os
from googleapiclient.http import HttpMockSequence


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


def mock_spreadsheet_instance(fixtures=list()):
    return mock_google_sheets_responses(['get_sheets.json'] + fixtures)


def mock_range_instance(fixtures=list()):
    return mock_google_sheets_responses(['get_sheets.json', 'people.json'] + fixtures)


def open_fixture(fixture_filename):
    fixture_folder_path = os.path.join(os.path.dirname(__file__), "fixtures/")
    return open(fixture_folder_path + fixture_filename).read()

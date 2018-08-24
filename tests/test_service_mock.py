from sheetfu.service import SheetsService
from googleapiclient.http import HttpMockSequence
from googleapiclient.discovery import Resource
from tests.utils import open_fixture


class TestServiceCreation:

    http_mocks = HttpMockSequence([
        ({'status': '200'}, open_fixture('discovery.json')),
        ({'status': '200'}, open_fixture('people.json'))
    ])

    def test_mock_instantiation(self):
        service = SheetsService().build(http=self.http_mocks)
        assert isinstance(service, Resource)

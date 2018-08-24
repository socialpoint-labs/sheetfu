# -*- coding: utf-8 -*-

"""
    sheetfu.client
    ~~~~~~~~~~~~~~

    Implement the SpreadsheetApp client .
    :copyright: © 2018 by Social Point Labs.
    :license: MIT, see LICENSE for more details.
"""


from sheetfu.service import SheetsService, DriveService
from sheetfu.model import Spreadsheet
import time


class SpreadsheetApp:

    def __init__(self, path_to_secret=None, http=None):
        """
        Client object which will slightly copy the API from the spreadsheet google app script API.
        This service assumes that you're connecting to the API with service to service credentials.

        For more info on how to create a secret.json for service to service connection refer to this page:
        https://developers.google.com/identity/protocols/OAuth2ServiceAccount

        :param path_to_secret: Absolute path where your service to service secret json credentials is located.
        :param http: Cache requests content (for mocks requests).
        This client creates 2 services:
            - One for spreadsheet manipulation.
            - One for Drive file and folder manipulation (mostly for giving editor/reader accesses to users).

        """
        self.sheet_service = SheetsService(path_to_secret=path_to_secret).build(http=http)
        if not http:        # if not mock
            self.drive_service = DriveService(path_to_secret=path_to_secret).build()

        self.batches = list()

    def create(self, name, editor=None):
        """
        Method to create a spreadsheet from scratch, given a name and an optional owner.
        :param name: The name to give to the new spreadsheet.
        :param editor: Add an owner to the spreadsheet (optional but recommended, otherwise only the service
        account can access the sheet and the sheet will remain invisible).
        :return: Spreadsheet Json Resource.
        """
        spreadsheet_body = {"properties": {"title": name}}
        request = self.sheet_service.spreadsheets().create(body=spreadsheet_body)
        response = request.execute()
        if editor is not None:
            time.sleep(3)       # needed to be sure the file is created and accessible (otherwise triggers 500).
            self.add_permission(response["spreadsheetId"], editor)
        return Spreadsheet(client=self, spreadsheet_id=response["spreadsheetId"])

    def add_permission(self, file_id, default_owner):   # todo: add multiple user types.
        """
        Add user owner permission to a file ID created by service account.
        :param file_id: The file ID that must be given permission.
        :param default_owner: User email address to give ownership of the file.
        :return:
        """
        user_permission = {
            'type': 'user',
            'role': 'writer',
            'emailAddress': default_owner
        }
        request = self.drive_service.permissions().create(
            fileId=file_id,
            body=user_permission,
            fields='id',
        )
        response = request.execute()
        return response

    def open_by_id(self, spreadsheet_id):
        """
        Open a spreadsheet for a given spreadsheet ID.
        :param spreadsheet_id.
        :return: Spreadsheet instance.
        """
        return Spreadsheet(client=self, spreadsheet_id=spreadsheet_id)

    def open_by_url(self, url):
        """
        Open a spreadsheet for a given url.
        :param url: The url of the target spreadsheet.
        :return: Spreadsheet instance.
        """
        url = url.replace("https://docs.google.com/spreadsheets/d/", "")
        spreadsheet_id = url[0: url.index('/')]
        return Spreadsheet(client=self, spreadsheet_id=spreadsheet_id)


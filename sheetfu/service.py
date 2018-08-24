# -*- coding: utf-8 -*-

"""
    sheetfu.service
    ~~~~~~~~~~~~~~

    Implement the Google Sheet and Google drive services to access, interact with, and give permission to spreadsheets.
    :copyright: © 2018 by Social Point Labs.
    :license: MIT, see LICENSE for more details.
"""


from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
from googleapiclient.discovery import build


class SheetsService:

    """Class to create ready to use sheets service with service to service credentials"""

    def __init__(self, path_to_secret=None):
        """
        :param path_to_secret: path to service to service json credentials file.
        """
        self.scopes = [
            'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/spreadsheets'
        ]
        self.path_to_secret = path_to_secret
        if self.path_to_secret is None:
            self.credentials = None
        else:
            self.credentials = ServiceAccountCredentials.from_json_keyfile_name(self.path_to_secret, self.scopes)

    def build(self, http=None):
        """
        Builds a sheet service, ready to query sheets.
        :param http: Only needed for unit testing. Must be an object of HttpMockSequence. DO NOT USE IN PROD.
        :return: An authorized sheets service.
        """
        if http is None:        # if not None must be instance of HttpMockSequence for unit testing
            http = self.credentials.authorize(Http())
        service = build('sheets', 'v4', http=http, cache_discovery=False)
        return service


class DriveService:

    """Class to create ready to use drive service with service to service credentials"""

    def __init__(self, path_to_secret=None):
        """
        :param path_to_secret: path to service to service json credentials file.
        """
        self.scopes = [
            'https://www.googleapis.com/auth/drive'
        ]
        self.path_to_secret = path_to_secret
        if self.path_to_secret is None:
            self.credentials = None
        else:
            self.credentials = ServiceAccountCredentials.from_json_keyfile_name(self.path_to_secret, self.scopes)

    def build(self, http=None):
        """
        Builds a sheet service, ready to query sheets.
        :param http: Only needed for unit testing. Must be an object of HttpMockSequence. DO NOT USE IN PROD.
        :return: An authorized sheets service.
        """
        if http is None:  # if not None must be instance of HttpMockSequence for unit testing
            http = self.credentials.authorize(Http())
        service = build('drive', 'v3', http=http, cache_discovery=False)
        return service


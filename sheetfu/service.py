# -*- coding: utf-8 -*-

"""
    sheetfu.service
    ~~~~~~~~~~~~~~

    Implement the Google Sheet and Google drive services to access, interact with, and give permission to spreadsheets.
    :copyright: © 2018 by Social Point Labs.
    :license: MIT, see LICENSE for more details.
"""
import json
import os
import tempfile

from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
from googleapiclient.discovery import build


class BaseService(object):

    SERVICE = ""
    VERSION = ""

    def __init__(self, path_to_secret=None, from_env=False):
        if from_env:
            config_dict = self._build_keyfile_dict()
            self.credentials = ServiceAccountCredentials.from_json_keyfile_dict(config_dict, self.scopes)
        else:
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
        service = build(self.SERVICE, self.VERSION, http=http, cache_discovery=False)
        return service

    @staticmethod
    def _build_keyfile_dict():
        return {
            "type": os.environ.get("SHEETFU_CONFIG_TYPE"),
            "project_id": os.environ.get("SHEETFU_CONFIG_PROJECT_ID"),
            "private_key_id": os.environ.get("SHEETFU_CONFIG_PRIVATE_KEY_ID"),
            "private_key": os.environ.get("SHEETFU_CONFIG_PRIVATE_KEY").replace('\\n', '\n'),
            "client_email": os.environ.get("SHEETFU_CONFIG_CLIENT_EMAIL"),
            "client_id": os.environ.get("SHEETFU_CONFIG_CLIENT_ID"),
            "auth_uri": os.environ.get("SHEETFU_CONFIG_AUTH_URI"),
            "token_uri": os.environ.get("SHEETFU_CONFIG_TOKEN_URI"),
            "auth_provider_x509_cert_url": os.environ.get("SHEETFU_CONFIG_AUTH_PROVIDER_URL"),
            "client_x509_cert_url": os.environ.get("SHEETFU_CONFIG_CLIENT_CERT_URL"),
        }


class SheetsService(BaseService):

    """Class to create ready to use sheets service with service to service credentials"""
    SERVICE = "sheets"
    VERSION = "v4"

    def __init__(self, path_to_secret=None, from_env=False):
        """
        :param path_to_secret: path to service to service json credentials file.
        :param from_env: bool to specify if config should be retrieved from ENV variables
        """
        self.scopes = [
            'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/spreadsheets'
        ]
        super(SheetsService, self).__init__(path_to_secret, from_env)


class DriveService(BaseService):

    """Class to create ready to use drive service with service to service credentials"""
    SERVICE = "drive"
    VERSION = "v3"

    def __init__(self, path_to_secret=None, from_env=False):
        """
        :param path_to_secret: path to service to service json credentials file.
        :param from_env: bool to specify if config should be retrieved from ENV variables
        """
        self.scopes = [
            'https://www.googleapis.com/auth/drive'
        ]
        super(DriveService, self).__init__(path_to_secret, from_env)



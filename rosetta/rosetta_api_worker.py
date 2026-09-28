from dotenv import load_dotenv
import os
import requests
import datetime
import json
from pprint import pprint

class RosettaAPIWorker:
    def __init__(self):
        self.base_url = ""
        self.token_url = ""
        self._client_id = ""
        self._client_secret = ""
        self._oath_token = ""
        self._oauth_scopes = ""
        self.test_id = ""
        self.export_location = ""
        self.expires_in = ""



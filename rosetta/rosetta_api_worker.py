import os
import requests
import datetime
import json

from .rosetta_person import RosettaPerson
from .rosetta_employee_association import RosettaEmployeeAssociation
from .rosetta_student_association import RosettaStudentAssociation

class RosettaAPIWorker:
    def __init__(self,base_url: str,token_url: str,client_id: str,client_secret: str):
        #Validate Parameters
        if not isinstance(base_url, str) or not base_url.strip():
            raise ValueError("Base URL is missing")

        if not isinstance(token_url, str) or not token_url.strip():
                    raise ValueError("Token URL is missing")

        if not isinstance(client_id, str) or not client_id.strip():
                    raise ValueError("Client ID is missing")

        if not isinstance(client_secret, str) or not client_secret.strip():
                    raise ValueError("Client Secret is missing")

        self.base_url = base_url
        self.token_url = token_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.oath_token = ""
        self.expires_in = ""



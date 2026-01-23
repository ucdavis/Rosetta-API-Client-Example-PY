'''
    Title: rosetta-api-client-example.py
    Authors: Dean Bunn and Wilson Miller
    Last Edit: 2026-01-23
'''

from dotenv import load_dotenv
import os
import requests
import datetime
import json

#Load the .env file
load_dotenv()

#Class for Rosetta API Information
class Rosetta_API_Info:
    def __init__(self):
        self.base_url = ""
        self.token_url = ""
        self.client_id = ""
        self.client_secret = ""
        self.oath_token = ""
        self.test_id = ""

#Class for Rosetta Person Information
class Rosetta_Person_Info:
    def __init__(self):
        self.iam_id = ""
        self.displayname = ""
        self.birth_date = ""
        self.manager_iam_id = ""
        self.provisioning_status_primary = ""
        self.name_lived_first_name = ""
        self.name_lived_middle_name = ""
        self.name_lived_last_name = ""
        self.name_legal_first_name = ""
        self.name_legal_middle_name = ""
        self.name_legal_last_name = ""
        self.id_iam_id = ""
        self.id_login_id = ""
        self.id_student_id = ""
        self.id_mothra_id = ""
        self.id_employee_id = ""
        self.id_mail_id = ""
        self.id_pidm = ""
        self.email_primary = ""
        self.email_work = ""
        self.email_personal = ""
        self.phone_primary = ""
        self.phone_personal = ""
        self.modified_date = ""

#Initiate Rosetta API Information Class and Load Required Values from .env file
ucdAPIInfo = Rosetta_API_Info()
ucdAPIInfo.base_url = os.getenv("ROSETTA_BASE_URL")
ucdAPIInfo.client_id = os.getenv("ROSETTA_CLIENT_ID")
ucdAPIInfo.client_secret = os.getenv("ROSETTA_CLIENT_SECRET")
ucdAPIInfo.token_url = os.getenv("ROSETTA_OAUTH_URL")
ucdAPIInfo.test_id = os.getenv("ROSETTA_TEST_ID")

#Check for Required Client ID and Secret Before Making API Calls
if(len(ucdAPIInfo.client_id) > 0 and len(ucdAPIInfo.client_secret) > 0):
    #Configure OAuth Header
    headersOAuthCall = {"client_id": ucdAPIInfo.client_id,
                        "client_secret": ucdAPIInfo.client_secret,
                        "grant_type":"CLIENT_CREDENTIALS",
                        "scope":"read:public read:sensitive"}
    
    #Make Rest Call to Token EndPoint to Get Access Token
    rtnTokenInfo = requests.post(ucdAPIInfo.token_url,headers=headersOAuthCall).json()

    #Check for Return Access Token
    if(len(rtnTokenInfo['access_token']) > 0):
        #Load Access Token (Good for 24 hours)
        ucdAPIInfo.oath_token = rtnTokenInfo['access_token']

        #Var for Header of Regular Endpoint Call
        headerEPCall = {"Authorization":"Bearer " + ucdAPIInfo.oath_token}

        #Var for People EndPoint Uri with User IAM ID
        peopleUri = ucdAPIInfo.base_url + "people?iamid=" + ucdAPIInfo.test_id

        #Make Rest Call to Pull Accounts Information
        peopleData = requests.get(peopleUri,headers=headerEPCall).json()

        #Loop Through Returned Users (Example Should Only be One)
        for peopleDatum in peopleData:
            #Initiate Rosetta Person
            ucdPersonInfo = Rosetta_Person_Info()
            ucdPersonInfo.iam_id = peopleDatum['iam_id']

            print(ucdPersonInfo.iam_id)



        




                   







    










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
from pprint import pprint

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
        self.affiliation = []
        self.employment_status = []
        self.student_association = []
        self.payroll_association = []

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

            #Check for IAM ID
            if "iam_id" in peopleDatum:
                ucdPersonInfo.iam_id = peopleDatum['iam_id']

            #Check for Display Name
            if "displayname" in peopleDatum:
                ucdPersonInfo.displayname = peopleDatum['displayname']

            #Check for Birth Date
            if "birth_date" in peopleDatum:
                ucdPersonInfo.birth_date = peopleDatum['birth_date']

            #Check for Manager IAM ID
            if "manager_iam_id" in peopleDatum:
                ucdPersonInfo.manager_iam_id = peopleDatum['manager_iam_id']

            #Check for Provisioning Statuses 
            if "provisioning_status" in peopleDatum and len(peopleDatum['provisioning_status']) > 0:

                #Loop Through Each Provisioning Status
                for provstat in peopleDatum['provisioning_status']:

                    #Primary Status 
                    if "primary" in provstat:
                        ucdPersonInfo.provisioning_status_primary = provstat['primary']
                    
            #Check for UCD Names
            if "name" in peopleDatum and len(peopleDatum['name']) > 0:

                #Loop Through Each UCD Name
                for um in peopleDatum['name']:

                    #Lived First Name
                    if "lived_first_name" in um:
                        ucdPersonInfo.name_lived_first_name = um['lived_first_name']

                    #Lived Middle Name
                    if "lived_middle_name" in um:
                        ucdPersonInfo.name_lived_middle_name = um['lived_middle_name']

                    #Lived Last Name
                    if "lived_last_name" in um:
                        ucdPersonInfo.name_lived_last_name = um['lived_last_name']

                    #Legal First Name
                    if "legal_first_name" in um:
                        ucdPersonInfo.name_legal_first_name = um['legal_first_name']

                    #Legal Middle Name
                    if "legal_middle_name" in um:
                        ucdPersonInfo.name_legal_middle_name = um['legal_middle_name']

                    #Legal Last Name
                    if "legal_last_name" in um:
                        ucdPersonInfo.name_legal_last_name = um['legal_last_name']

            #Check for UCD IDs
            if "id" in peopleDatum and len(peopleDatum['id']) > 0:

                #Loop Through Each UCD ID
                for ucdid in peopleDatum['id']:

                    #IAM ID
                    if "iam_id" in ucdid:
                        ucdPersonInfo.id_iam_id = ucdid['iam_id']

                    #Login ID
                    if "login_id" in ucdid:
                        ucdPersonInfo.id_login_id = ucdid['login_id']

                    #Student ID
                    if "student_id" in ucdid:
                        ucdPersonInfo.id_student_id = ucdid['student_id']

                    #Mothra ID
                    if "mothra_id" in ucdid:
                        ucdPersonInfo.id_mothra_id = ucdid['mothra_id']

                    #Employee ID
                    if "employee_id" in ucdid:
                        ucdPersonInfo.id_employee_id = ucdid['employee_id']

                    #Mail ID
                    if "mail_id" in ucdid:
                        ucdPersonInfo.id_mail_id = ucdid['mail_id']

                    #PIDM
                    if "pidm" in ucdid:
                        ucdPersonInfo.id_pidm = ucdid['pidm']

                    
            #Check for Email Addressees
            if "email" in peopleDatum and len(peopleDatum['email']) > 0:

                #Loop Through Each Email Address
                for ucdeml in peopleDatum['email']:

                    #Primary Email Address
                    if "primary" in ucdeml:
                        ucdPersonInfo.email_primary = ucdeml['primary']

                    #Work Email Address
                    if "work" in ucdeml:
                        ucdPersonInfo.email_work = ucdeml['work']

                    #Personal Email Address
                    if "personal" in ucdeml:
                        ucdPersonInfo.email_personal = ucdeml['personal']


            #Check for Phones
            if "phone" in peopleDatum and len(peopleDatum['phone']) > 0:

                #Loop Through Each Phone Entry
                for phne in peopleDatum['phone']:

                    #Primary Phone
                    if "primary" in phne:
                        ucdPersonInfo.phone_primary = phne['primary']

                    if "personal" in phne:
                        ucdPersonInfo.phone_personal = phne['personal']

                    
            #Check for Affiliations
            if "affiliation" in peopleDatum and len(peopleDatum['affiliation']) > 0:

                #Loop Through Each Affiliation
                for ucdafl in peopleDatum['affiliation']:
                    ucdPersonInfo.affiliation.append(ucdafl)

            
            #

            pprint(ucdPersonInfo.__dict__)






        




                   







    










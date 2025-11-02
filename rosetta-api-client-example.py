'''
    Title: rosetta-api-client-example.py
    Authors: Dean Bunn and Wilson Miller
    Last Edit: 2025-11-02
'''

from dotenv import load_dotenv
import os
import requests
import datetime

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

#Initiate Rosetta API Information Class and Load Required Values from .env file
ucdAPIInfo = Rosetta_API_Info()
ucdAPIInfo.base_url = os.getenv("ROSETTA_BASE_URL")
ucdAPIInfo.client_id = os.getenv("ROSETTA_CLIENT_ID")
ucdAPIInfo.client_secret = os.getenv("ROSETTA_CLIENT_SECRET")
ucdAPIInfo.token_url = os.getenv("ROSETTA_OAUTH_URL")

#Check for Required Client ID and Secret Before Making API Calls
if(len(ucdAPIInfo.client_id) > 0 and len(ucdAPIInfo.client_secret) > 0):
    #Configure OAuth Header
    headersOAuthCall = {"client_id": ucdAPIInfo.client_id,
                        "client_secret": ucdAPIInfo.client_secret,
                        "grant_type":"CLIENT_CREDENTIALS"}
    
    #Make Rest Call to Token EndPoint to Get Access Token
    rtnTokenInfo = requests.post(ucdAPIInfo.token_url,headers=headersOAuthCall).json()

    #Check for Return Access Token
    if(len(rtnTokenInfo['access_token']) > 0):
        ucdAPIInfo.oath_token = rtnTokenInfo['access_token']

    print(ucdAPIInfo.oath_token)










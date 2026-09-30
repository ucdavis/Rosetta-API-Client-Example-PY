
from dotenv import load_dotenv
import os

#Import Rosetta Classes
from rosetta import RosettaAPIWorker, RosettaPerson, RosettaEmployeeAssociation, RosettaStudentAssociation


def main():

    #Load the .env file
    load_dotenv()

    #Initialize Rosetta API Worker
    rosetta_api_wrkr = RosettaAPIWorker(os.getenv("ROSETTA_BASE_URL"),
                                        os.getenv("ROSETTA_OAUTH_URL"),
                                        os.getenv("ROSETTA_CLIENT_ID"),
                                        os.getenv("ROSETTA_CLIENT_SECRET"))

    
    
    



#Standard Main Function Setup
if __name__ == "__main__":
    main()





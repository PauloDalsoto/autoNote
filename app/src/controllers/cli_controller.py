import inquirer
from termcolor import colored

from src.services.sap_service import SAPService

class CLIController:
    def __init__(self):
        self.sap_service = SAPService()

    def welcome(self):
        print(colored("Welcome to AutoNote!", "green", attrs=["bold"]))

    def confirm_notes_input(self):
        inquirer.confirm(message="Proceed?").execute()
    
      
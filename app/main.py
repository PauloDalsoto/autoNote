from termcolor import colored
from src.controllers.cli_controller import CLIController
from InquirerPy import inquirer

def main():
    cli_controller = CLIController()

    cli_controller.welcome()

    # cli_controller.confirm_notes_input()
    proceed, service, confirm = False, False, False
    proceed = inquirer.confirm(message="Proceed?", default=True).execute()
    if proceed:
        service = inquirer.confirm(message="Require 1 on 1?").execute()
    if service:
        confirm = inquirer.confirm(message="Confirm?").execute()


if __name__ == "__main__":
    main()
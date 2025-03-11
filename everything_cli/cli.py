# main entry point for command line interface
from everything_cli.utils.input_handler import validate_user_input


def main():
    while True:
        choice = validate_user_input()
        if choice == "2":
            print("exiting cli...")
            break
        print(f"You selected option: {choice}")


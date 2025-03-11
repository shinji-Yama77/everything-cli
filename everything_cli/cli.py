# main entry point for command line interface
from everything_cli.utils.input_handler import validate_user_input
from everything_cli.commands.chatgpt import chatgpt_command


def main():
    while True:
        choice = validate_user_input()
        if choice == "3":
            chatgpt_command()


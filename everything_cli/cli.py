# main entry point for command line interface
from everything_cli.utils.input_handler import validate_user_input
from everything_cli.commands.chatgpt import chatgpt_command
from everything_cli.utils.menu import showing_animation, show_logo

# We need a command dispatcher



def main():

    print("\n=== The Mega CLI Tool ===")
    show_logo()
    showing_animation()
    print("\n[ EVERYTHING-CLI ] - Automate Your Work Easily\n")
    while True:
        choice = validate_user_input()
        if choice == "3":
            chatgpt_command()


# main entry point for command line interface
from everything_cli.utils.input_handler import validate_user_input
from everything_cli.commands.chatgpt import chatgpt_command
from everything_cli.utils.menu import showing_animation, show_logo
from everything_cli.utils.llama_indexing import build_index
import os
# We need a command dispatcher





COMMANDS = {
    "1": lambda: print("Feature coming soon"), # we use lambda because we don't want to immedaitely print
    "2": lambda: print("Exiting cli"),
    "3": chatgpt_command, # we store the function reference
    "4": build_index
}


def main():

    print("Current Working Directory:", os.getcwd())        
    print("\n=== The Mega CLI Tool ===")
    show_logo()
    showing_animation()
    print("\n[ EVERYTHING-CLI ] - Automate Your Work Easily\n")
    while True:
        choice = validate_user_input()
        if choice in COMMANDS:
            COMMANDS[choice]() # executes the function dynamically
            break
        else:
            print("INvalid choice. Please enter a valid option.")


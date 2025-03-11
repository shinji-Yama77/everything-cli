from everything_cli.utils.menu import display_menu, options

def validate_user_input():
    """Ensures user enters a valid menu choice."""

    # set allows constant lookup time
    valid_choices = set(options.keys())

    while True:
        choice = display_menu()
        if choice in valid_choices:
            return choice 
        # .join allows elements of list or set to be combined with specified separator
        print(f"Invalid choice. Please enter one of : {', '.join(valid_choices)}")



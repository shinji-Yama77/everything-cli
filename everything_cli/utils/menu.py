options = {
        "1": "Greet someone",
        "2": "Exit",
        "3": "ChatGPT Help"
    }


def display_menu():
    """Display the CLI menu and return the user's choice."""
    print("\n=== The Mega CLI Tool ===")
    for key, value in options.items():
        print(f"{key}. {value}")

    return input("Enter your choice: ").strip()



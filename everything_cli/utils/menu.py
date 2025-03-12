from rich.progress import Progress
import time

options = {
        "1": "Greet someone",
        "2": "Exit",
        "3": "ChatGPT Help",
        "4": "Build index"
    }


def show_logo():
    print(r""" __       __  ________   ______    ______  
|  \     /  \|        \ /      \  /      \ 
| $$\   /  $$| $$$$$$$$|  $$$$$$\|  $$$$$$\
| $$$\ /  $$$| $$__    | $$ __\$$| $$__| $$
| $$$$\  $$$$| $$  \   | $$|    \| $$    $$
| $$\$$ $$ $$| $$$$$   | $$ \$$$$| $$$$$$$$
| $$ \$$$| $$| $$_____ | $$__| $$| $$  | $$
| $$  \$ | $$| $$     \ \$$    $$| $$  | $$
 \$$      \$$ \$$$$$$$$  \$$$$$$  \$$   \$$
    """)

def showing_animation():
    # with allows us to clean system resources after it exiits
    with Progress() as progress:
        # add a total of 100 steps
        task = progress.add_task("[cyan]Loading CLI...", total=100)
        for i in range(100):
            time.sleep(0.02) # simulate loading
            # update task 1 step each time
            progress.update(task, advance=1)


def display_menu():
    """Display the CLI menu and return the user's choice."""
    for key, value in options.items():
        print(f"{key}. {value}")

    return input("Enter your choice: ").strip()




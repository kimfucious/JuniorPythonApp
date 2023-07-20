from art import text2art
from termcolor import colored
from enums import WishStatus
import json
import os
import random
import sys
import termios  # For Unix-based systems
import tty  # For Unix-based systems


def clear_screen():
    # For Windows
    if os.name == "nt":
        os.system("cls")
    # For macOS and Linux
    else:
        os.system("clear")
    return


def get_adj():
    words = [
        "Amazing",
        "Awesome",
        "Cool",
        "Fantastic",
        "Great",
        "Magical",
        "Super",
        "Ultimate",
        "Wonderful",
    ]
    return random.choice(words)


def get_color():
    colors = ["cyan", "magenta", "yellow", "green", "blue", "red"]
    return random.choice(colors)


def print_ascii_art(text):
    color = get_color()
    word = get_adj()
    art_1 = text2art("The " + word + " " + text, font="small")
    print(colored(art_1, color))


def quit_app():
    clear_screen()
    print(colored("\n🌺 Aloha!", "green"))
    exit()


def wish_status_serializer(obj):
    if isinstance(obj, WishStatus):
        return obj.value
    raise TypeError(
        "Object of type {0} is not JSON serializable".format(type(obj))
    )


class WishStatusEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, WishStatus):
            return obj.value
        return super().default(obj)


def wait_for_keypress():
    try:
        # Attempt to use msvcrt for Windows
        import msvcrt

        _ = msvcrt.getch()
    except ImportError:
        # Fall back to tty for Unix-based systems
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            _ = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

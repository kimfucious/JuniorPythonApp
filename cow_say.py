import cowsay
import random
from helpers import clear_screen, print_ascii_art

chars = [
    "beavis",
    "cheese",
    "cow",
    "daemon",
    "dragon",
    "fox",
    "ghostbusters",
    "kitty",
    "meow",
    "miki",
    "milk",
    "pig",
    "stegosaurus",
    "stimpy",
    "trex",
    "turkey",
    "turtle",
    "tux",
]


def print_cowsay(text, char):
    clear_screen()
    print(cowsay.get_output_string(char, text))


def run_cowsay():
    clear_screen()
    print_ascii_art("Cow Say")
    text = input("🐄 What does the cow say? ")

    if not text.strip():
        return run_cowsay()

    print("\n🐄 Available characters:")
    for i, character in enumerate(chars, start=1):
        print(f"{i}. {character}")

    choice = input("\n🐄 Enter the number of the character or press Enter: ")
    if choice and choice.isdigit() and 1 <= int(choice) <= len(chars):
        character = chars[int(choice) - 1]
    else:
        character = random.choice(chars)

    print_cowsay(text, character)

from countries import search_country
from cow_say import run_cowsay
from dad_jokes import get_dad_joke
from yo_mama import get_yo_mama_joke
from halo import Halo
from helpers import (
    clear_screen,
    get_laugh_emoji,
    print_ascii_art,
    quit_app,
    wait_for_keypress,
)
from termcolor import colored
from wish_list import run_wishlist

menu_options = {
    1: "(D)ad Joke",
    2: "(Y)o Mama Joke",
    3: "(C)owsay",
    4: "(F)ind Flag",
    5: "(W)ish List",
    6: "(Q)uit",
}


def init_menu():
    clear_screen()
    run_menu()


def print_menu():
    for key in menu_options.keys():
        print(f"{key}. {menu_options[key]}")


def dad_joke():
    print(" ")
    spinner = Halo(text="Getting Dad Joke...", spinner="dots")
    spinner.start()
    joke = get_dad_joke()
    spinner.stop()
    print(joke + "\n")
    print(f"{get_laugh_emoji()} Press any key to continue")
    wait_for_keypress()
    clear_screen()


def yo_mama_joke():
    print(" ")
    spinner = Halo(text="Getting Yo mama Joke...", spinner="dots")
    spinner.start()
    joke = get_yo_mama_joke()
    spinner.stop()
    print(joke + "\n")
    print(f"{get_laugh_emoji()} Press any key to continue")
    wait_for_keypress()
    clear_screen()


def cowsay():
    run_cowsay()
    print("\n🐄 Press any key to continue")
    wait_for_keypress()
    clear_screen()


def get_flag():
    country = input("\nName a country: ")
    print(" ")
    spinner = Halo(text="Finding flag...", spinner="earth", interval=180)
    spinner.start()
    message = search_country(country)
    spinner.stop()
    print(f"{message} . Press any key to continue")
    wait_for_keypress()
    clear_screen()


def wishlist():
    clear_screen()
    run_wishlist()


def run_menu():
    while True:
        option = ""
        print_ascii_art("App")
        print_menu()
        try:
            option = input("\nEnter your choice: ")
            if option.lower() == "":
                clear_screen()
            elif option.lower() == "d":
                dad_joke()
            elif option.lower() == "y":
                yo_mama_joke()
            elif option.lower() == "c":
                cowsay()
            elif option.lower() == "f":
                get_flag()
            elif option.lower() == "w":
                wishlist()
            elif option.lower() == "q":
                quit_app()
            else:
                option = int(option)
        except ValueError:
            print(colored("\n💣 Please select a valid menu option.", "yellow"))
            print(colored("\nPress any key to continue", "cyan"))
            wait_for_keypress()
            clear_screen()

        if option == 1:
            dad_joke()
        elif option == 2:
            yo_mama_joke()
        elif option == 3:
            cowsay()
        elif option == 4:
            get_flag()
        elif option == 5:
            wishlist()
        elif option == 6:
            quit_app()
        else:
            clear_screen()

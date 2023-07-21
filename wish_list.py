import data
from enums import WishStatus
from helpers import (
    clear_screen,
    get_genie_tagline,
    print_ascii_art,
    quit_app,
    wait_for_keypress,
    wish_status_serializer,
)

from termcolor import colored
from wish_menu import run_wish_menu
import json
import requests

wishlist_menu_options = {
    "w": "Make another Wish",
    "x": "Exit Wish List",
    "q": "Quit",
}

wishlist_menu_options_no_wishes = {
    "x": "Exit Wish List",
    "q": "Quit",
}


def print_wishlist_menu():
    number_of_wishes = len(data.wishes)
    if number_of_wishes == 3:
        for key in wishlist_menu_options_no_wishes.keys():
            print(f" {key}. {wishlist_menu_options[key]}")
    else:
        for key in wishlist_menu_options.keys():
            print(f" {key}. {wishlist_menu_options[key]}")


def get_wishes():
    api_url = "http://127.0.0.1:5000/items"
    headers = {"Accept": "application/json"}
    resp = requests.get(api_url, headers=headers)
    items = resp.json()
    data.wishes = items
    return data.wishes


def list_wishes():
    api_url = "http://127.0.0.1:5000/items"
    headers = {"Accept": "application/json"}
    resp = requests.get(api_url, headers=headers)
    wishes = resp.json()
    number_of_wishes = len(wishes)
    print("🙏🏽 Here are your wishes, Master:\n")
    for i, wish in enumerate(wishes, start=1):
        print(f" {i}. {wish['description']} ({wish['status']})")

    print("\nSelect a wish by number or...\n")
    print_wishlist_menu()
    option = input("\nWhat is your desire?: ")

    if option == "":
        clear_screen()
    elif option.lower() == "q":
        quit_app()
    elif option.lower() == "w" and number_of_wishes < 3:
        clear_screen()
        return "w"
    elif option.lower() == "x":
        clear_screen()
        return "x"
    else:
        try:
            option = int(option)
            if option <= number_of_wishes:
                clear_screen()
                run_wish_menu(wishes[option - 1])
            else:
                clear_screen()
        except ValueError:
            clear_screen()


def make_a_wish():
    wish_text = input("🧞 Make a wish ('q' to quit): ")
    if wish_text.lower() == "q":
        quit_app()
    if wish_text == "":
        print("\n🧞 Please enter a wish")
        print("\nPress any key to continue")
        wait_for_keypress()
        clear_screen()
        return
    api_url = "http://127.0.0.1:5000/items"
    headers = {
        "Accept": "application/json",
        "content-type": "application/json",
    }
    wish = {"description": wish_text, "status": WishStatus.UNFULFILLED}
    payload = json.dumps(
        wish,
        default=wish_status_serializer,
    )

    try:
        resp = requests.post(api_url, data=payload, headers=headers)
        resp.raise_for_status()
        data.wishes.append(resp.json())

        if resp.status_code == 201:
            print(
                f"\n🧞 {get_genie_tagline()}.  Press any key to continue."
            )
            wait_for_keypress()
        else:
            print(colored("\nSomething went wrong. Please try again.", "red"))
            print(colored("\nPress any key to continue", "cyan"))
            wait_for_keypress()

    except requests.exceptions.RequestException as e:
        print(colored(f"\nSomething went wrong: {e}", "red"))
        print(colored("\nPress any key to continue", "cyan"))
        wait_for_keypress()

    clear_screen()


def wishlist_option3():
    print("handle wishlist option 3")


def wishlist_option4():
    print("handle wishlist option 4")


def wishlist_option5():
    print("handle wishlist option 5")


def wishlist_option6():
    print("handle wishlist option 5")


def run_wishlist():
    data.init()
    get_wishes()
    while True:
        number_of_wishes = len(data.wishes)
        print_ascii_art("Wish List")
        if number_of_wishes == 0:
            make_a_wish()
        else:
            action = list_wishes()
            if action == "w":
                clear_screen()
                print_ascii_art("Wish List")
                make_a_wish()
            elif action == "x":
                break

from enums import WishStatus
from helpers import (
    clear_screen,
    print_ascii_art,
    quit_app,
    wait_for_keypress,
    wish_status_serializer,
    # WishStatusEncoder,
)

# from models import PartialWish
from termcolor import colored
from wish_menu import run_wish_menu
import json
import requests

wishes = []

wishlist_menu_options = {
    1: "Show Wish List",
    2: "Make a Wish",
    3: "Delete Wish",
    4: "Update Wish",
    5: "Exit Wish List",
    6: "Quit",
}


def print_wishlist_menu():
    for key in wishlist_menu_options.keys():
        print(f"{key}. {wishlist_menu_options[key]}")


def get_wishes():
    api_url = "http://127.0.0.1:5000/items"
    headers = {"Accept": "application/json"}
    resp = requests.get(api_url, headers=headers)
    items = resp.json()
    global wishes
    wishes = items
    return wishes


def wishlist_option1():
    api_url = "http://127.0.0.1:5000/items"
    headers = {"Accept": "application/json"}
    resp = requests.get(api_url, headers=headers)
    wishes = resp.json()
    number_of_wishes = len(wishes)
    if number_of_wishes == 0:
        print("\n😿 You've yet to make any wishes")
        print("\nPress any key to continue")
        wait_for_keypress()
        clear_screen()
    else:
        print("\n🙏🏽 Here are your wishes, Master:\n")
        for i, wish in enumerate(wishes, start=1):
            print(f"{i}. {wish['description']} ({wish['status']})")

        option = input("\nSelect a Wish or Press ENTER: ")

        if option == "":
            clear_screen()
        else:
            option = int(option)
            if option <= number_of_wishes:
                clear_screen()
                run_wish_menu(wishes[option - 1])
            else:
                clear_screen()


def wishlist_option2():
    wish_text = input("\n🧞 Make a wish: ")
    api_url = "http://127.0.0.1:5000/items"
    headers = {
        "Accept": "application/json",
        "content-type": "application/json",
    }
    # wish = PartialWish(description=wish_text, status=WishStatus.UNFULFILLED)
    wish = {"description": wish_text, "status": WishStatus.UNFULFILLED}
    data = json.dumps(
        wish,
        default=wish_status_serializer,
    )

    resp = requests.post(api_url, data=data, headers=headers)
    if resp.status_code == 204:
        print(
            "\n🧞 Your wish is my command, Master.  Press any key to continue."
        )
        wait_for_keypress()
    else:
        print(colored("\nSomething went wrong. Please try again.", "red"))
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
    # get_wishes()
    # if len(wishes) == 0:
    #     print
    #     clear_screen()
    while True:
        option = ""
        print_ascii_art("Wish List")
        print_wishlist_menu()
        try:
            option = input("\nEnter your choice: ")
            if option == "q":
                quit_app()
            else:
                option = int(option)
        except ValueError:
            print(colored("\n💣 Please select a valid menu option.", "yellow"))
            print(colored("\n Press any key to continue", "cyan"))
            wait_for_keypress()
            clear_screen()

        if option == 1:
            wishlist_option1()
        elif option == 2:
            wishlist_option2()
        elif option == 3:
            wishlist_option3()
        elif option == 4:
            wishlist_option4()
        elif option == 5:
            clear_screen()
            break
        elif option == 6:
            quit_app()

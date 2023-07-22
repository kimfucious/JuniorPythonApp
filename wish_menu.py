from enums import WishStatus
from termcolor import colored
from helpers import (
    clear_screen,
    get_genie_tagline,
    print_ascii_art,
    quit_app,
    wait_for_keypress,
    wish_status_serializer,
)
import data
import json
import os
import requests

BASE_URL = os.environ.get("API_BASE_URL")
WISHES_URL = f"{BASE_URL}/wishes"

wish_menu_options = {
    1: "Mark as fulfilled",
    2: "Change",
    3: "Delete",
    4: "Back",
    5: "Quit",
}


def print_wish_menu():
    for key in wish_menu_options.keys():
        print(f"{key}. {wish_menu_options[key]}")


def fulfill_wish(item):
    headers = {
        "Accept": "application/json",
        "content-type": "application/json",
    }
    payload = json.dumps(
        {**item, "status": WishStatus.FULFILLED},
        default=wish_status_serializer,
    )
    try:
        resp = requests.patch(WISHES_URL, data=payload, headers=headers)
        resp.raise_for_status()
        print(f"\n🧞 {get_genie_tagline()}.  Press any key to continue.")
        wait_for_keypress()
    except requests.exceptions.RequestException as e:
        print(colored(f"\nSomething went wrong: {e}", "red"))
        print(colored("\nPress any key to continue", "cyan"))
        wait_for_keypress()

    clear_screen()


def change_wish(item):
    user_input = input(
        "\n🧞 What will your wish be now? (Press ENTER to cancel): "
    )
    if not user_input:
        clear_screen()
        return
    headers = {
        "Accept": "application/json",
        "content-type": "application/json",
    }
    payload = json.dumps(
        {**item, "description": user_input},
        default=wish_status_serializer,
    )
    try:
        resp = requests.patch(WISHES_URL, data=payload, headers=headers)
        resp.raise_for_status()
        print(f"\n🧞 {get_genie_tagline()}.  Press any key to continue.")
        wait_for_keypress()
    except requests.exceptions.RequestException as e:
        print(colored(f"\nSomething went wrong: {e}", "red"))
        print(colored("\nPress any key to continue", "cyan"))
        wait_for_keypress()

    clear_screen()


def delete_wish(item):
    user_input = input(
        colored(
            f"This will delete your wish, '{item['description']}'.  Are you sure? (y/N): ",  # noqa: E501
            "red",
        )
    )
    if user_input.lower() == "y":
        try:
            url = f"{WISHES_URL}?id={item['id']}"
            headers = {
                "Accept": "application/json",
                "content-type": "application/json",
            }
            resp = requests.delete(url, headers=headers)
            resp.raise_for_status()

            for wish in data.wishes:
                if item["id"] == wish["id"]:
                    data.wishes.remove(wish)

            print(f"\n🧞 {get_genie_tagline()}.  Press any key to continue.")
            wait_for_keypress()
            clear_screen()
            return

        except requests.exceptions.RequestException as e:
            print(colored(f"\nSomething went wrong: {e}", "red"))
            print(colored("\nPress any key to continue", "cyan"))
            wait_for_keypress()
            clear_screen()
    else:
        clear_screen()
        return


def run_wish_menu(item):
    while True:
        option = ""
        print_ascii_art("Wish List")
        print(f"🧞 What should I do with '{item['description']}'?\n")
        print_wish_menu()
        try:
            option = input("\nEnter your choice: ")
            if option == "q":
                quit_app()
            else:
                option = int(option)
        except ValueError:
            print(colored("\n💣 Please select a valid menu option.", "yellow"))
            print(colored("\nPress any key to continue", "cyan"))
            wait_for_keypress()
            clear_screen()

        if option == 1:
            fulfill_wish(item)
            break
        elif option == 2:
            change_wish(item)
            break
        elif option == 3:
            delete_wish(item)
            break
        elif option == 4:
            clear_screen()
            break
        elif option == 5:
            quit_app()
        else:
            clear_screen()

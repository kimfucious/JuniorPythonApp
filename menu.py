from cow_say import run_cowsay
from dad_jokes import get_dad_joke
from yo_mama import get_yo_mama_joke
from halo import Halo
from helpers import clear_screen, print_ascii_art, quit_app, wait_for_keypress
from termcolor import colored
from wish_list import run_wishlist

menu_options = {
    1: "Dad Joke",
    2: "Yo Mama Joke",
    3: "Cowsay",
    4: "Wish List",
    5: "Quit",
}


def init_menu():
    clear_screen()
    run_menu()


def print_menu():
    for key in menu_options.keys():
        print(f"{key}. {menu_options[key]}")


def option1():
    spinner = Halo(text="\nGetting Dad Joke...", spinner="dots")
    spinner.start()
    joke = get_dad_joke()
    spinner.stop()
    print("\n" + joke + "\n")
    print("🤣 Press any key to continue")
    wait_for_keypress()
    clear_screen()


def option2():
    spinner = Halo(text="\nGetting Yo mama Joke...", spinner="dots")
    spinner.start()
    joke = get_yo_mama_joke()
    spinner.stop()
    print("\n" + joke + "\n")
    print("😹 Press any key to continue")
    wait_for_keypress()
    clear_screen()


def option3():
    run_cowsay()
    print("\n🐄 Press any key to continue")
    wait_for_keypress()
    clear_screen()


def option4():
    clear_screen()
    run_wishlist()


def run_menu():
    while True:
        option = ""
        print_ascii_art("App")
        print_menu()
        try:
            # option = int(input("\nEnter your choice: "))
            option = input("\nEnter your choice: ")
            if option.lower() == "q":
                quit_app()
            else:
                option = int(option)
        except ValueError:
            print(colored("\n💣 Please select a valid menu option.", "yellow"))
            print(colored("\nPress any key to continue", "cyan"))
            wait_for_keypress()
            clear_screen()

        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            quit_app()

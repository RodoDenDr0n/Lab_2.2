import json
from termcolor import colored


def read_json_file(path_to_file):
    """
    This function reads json file
    """
    with open(path_to_file, "r") as file:
        data = json.load(file)
    return data


def choosing_post(data):
    """
    This function is responsible for choosing post or the special object
    """
    print(colored("\nAvailable posts:", "cyan", attrs=["bold"]))
    for i in range(len(data)):
        post = colored("[+] ", 'green') + f"Post {i+1}"
        print(post)
    user_post = int(input(colored("Choose the post number to get information from: ", "blue", attrs=["bold"]) +
                          colored("\n>>> ", 'red', attrs=['bold'])))
    if type(data) == list:
        user_post = data[user_post-1]
    else:
        user_post = data
    return user_post


def choosing_information(shown_possible_choices):
    """
    This function is responsible for getting user's information choice
    """
    shown_possible_choices = "\n".join(shown_possible_choices)
    print(shown_possible_choices)
    user_choice = input(colored("Choose the name or number of section"
                        " that will be shown to you:", "blue", attrs=["bold"]) +
                        colored("\n>>> ", 'red', attrs=['bold']))
    try:
        user_choice = int(user_choice) - 1
    except ValueError:
        pass
    return user_choice


def printing_or_navigating(element):
    """
    This function is responsible for deciding whether
    to print or navigate element
    """
    element_type = ""
    if type(element) == dict:
        element_type = "dictionary"
    elif type(element) == list:
        element_type = "list"
        if len(element) == 0:
            return None
    print_or_navigate = input("\nType " + colored("print", 'green', attrs=['bold']) +
                              f" to get elements in {element_type}\n" 
                              "or type " + colored("explore", 'green', attrs=['bold']) + " to navigate elements:" +
                              colored("\n>>> ", 'red', attrs=['bold']))
    if print_or_navigate == 'print':
        return True
    elif print_or_navigate == 'explore':
        return False
    else:
        return printing_or_navigating(element)


def navigate_list(data):
    """
    This function is responsible for navigation in lists
    """
    while True:
        print(colored("\nInformation in your data: ", "cyan", attrs=["bold"]))
        possible_choices = [element for element in data]
        possible_choices = list(possible_choices)

        show_possible_choices = []
        number = 0
        for choice in possible_choices:
            number += 1
            choice = colored(f" [{number}] ", "green") + colored(choice, "white")
            show_possible_choices.append(choice)
        user_choice = choosing_information(show_possible_choices)

        if user_choice == "back":
            return None
        elif type(user_choice) == int:
            if type(data) == dict:
                values_list = list(data.values())
            else:
                values_list = data
            chosen_info = values_list[user_choice]
        else:
            chosen_info = data[user_choice]

        if type(chosen_info) == dict:
            value = printing_or_navigating(chosen_info)
            if value:
                print(chosen_info)
            elif value is False:
                navigate_dictionary(chosen_info)
            else:
                print(chosen_info)

        elif type(chosen_info) == list:
            value = printing_or_navigating(chosen_info)
            if value:
                print(chosen_info)
            elif value is False:
                navigate_list(chosen_info)
            else:
                print(chosen_info)
        else:
            print(chosen_info)


def navigate_dictionary(data):
    """
    This function is responsible for navigating information in dictionaries
    """
    while True:
        print(colored("\nInformation in your data: ", "cyan", attrs=["bold"]))
        possible_choices = list(data.keys())

        show_possible_choices = []
        number = 0
        for choice in possible_choices:
            number += 1
            choice = colored(f" [{number}] ", "green") + colored(choice, "white")
            show_possible_choices.append(choice)
        user_choice = choosing_information(show_possible_choices)

        if user_choice == "back":
            return None
        elif type(user_choice) == int:
            if type(data) == dict:
                values_list = list(data.values())
            else:
                values_list = data
            chosen_info = values_list[user_choice]
        else:
            chosen_info = data[user_choice]

        if type(chosen_info) == dict:
            value = printing_or_navigating(chosen_info)
            if value:
                print(chosen_info)
            elif value is False:
                navigate_dictionary(chosen_info)
            else:
                print(chosen_info)

        elif type(chosen_info) == list:
            value = printing_or_navigating(chosen_info)
            if value:
                print(chosen_info)
            elif value is False:
                navigate_list(chosen_info)
            else:
                print(chosen_info)
        else:
            print(chosen_info)


def main():
    """
    The main function that starts the program and gets
    the information about a file name that needs to be
    explored
    """
    path_to_file = input("Enter a " + colored("file name", "green", attrs=['bold']) + " to be explored:\n" +
                         colored(">>> ", "red", attrs=['bold']))
    data = read_json_file(path_to_file)
    user_post = choosing_post(data)
    if type(user_post) == dict:
        navigate_dictionary(user_post)
    else:
        navigate_list(user_post)


main()

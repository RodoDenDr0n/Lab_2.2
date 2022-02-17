# Lab_2.2
## About the project
This project was about creating module that will be able to work with json files and navigate with them. This would much simplify the process of getting needed information from json files.
## Functions used in the project
- read_json_file()
- choosing_post()
- choosing_information()
- printing_or_navigating()
- navigate_list()
- navigate_dictionary()
- main()
## read_json_file()
This function takes the path to the json file and reads it
```python
with open(path_to_file, "r") as file:
        data = json.load(file)
    return data
```
## choosing_post()
This function is responsible for choosing the first object to work with in json file. In our case, this function works with twitter posts.
```python
def choosing_post(data):
    ...
    if type(data) == list:
        user_post = data[user_post-1]
    else:
        user_post = data
    return user_post
```
If data type is dictionary and, thus, is a collection of posts, function assignes the data value to the user_post. If the data type is list, fuction chooses the entered user's value
## choosing_information()
This function takes the possible values and shows them for user for him/her to choose. Afterwards function returns the user's choice 
```python
def choosing_information(shown_possible_choices):
    shown_possible_choices = "\n".join(shown_possible_choices)
        print(shown_possible_choices)
        user_choice = input(...)
        try:
            user_choice = int(user_choice) - 1
        except ValueError:
            pass
        return user_choice
```
If user choice cannot be transformed into int type (that means user wants to search information not by number, but name) then exception is raised.
- <!> User also may write ```"back"``` in order to choose previous information
## printing_or_navigating()
This function takes the element which is dictionary or list and makes user make a decision whether to print information out, or to navigate it. If user desides to print information returns True, if not then returns False. If user misspelled the word, recalls the function
```python
def printing_or_navigating(element):
    ...
    if print_or_navigate == 'print':
        return True
    elif print_or_navigate == 'explore':
        return False
    else:
        return printing_or_navigating(element)
```
## navigate_list()
This function takes the data returned by the ```choosing_post()``` or ```navigate_dictionary()``` or ```navigate_list()``` function and is responsible for navigating the list object. This fucntion also calls ```choosing_information()```, ```printing_or_navigating()``` and one of ```navigate_list()``` or ```navigate_dictionary()``` functions. This function is also in the ```while True``` cycle so that it is recursive
```python
def navigate_list(data):
    while True:
        ...

        user_choice = choosing_information(show_possible_choices)
        ...

        if type(chosen_info) == dict:
            value = printing_or_navigating(chosen_info)
            ...

        elif type(chosen_info) == list:
            value = printing_or_navigating(chosen_info)
            ...
```
## navigate_dictionary()
This function takes the data returned by the ```choosing_post()``` or ```navigate_dictionary()``` or ```navigate_list()``` function and is responsible for navigating the dictionary object. This fucntion also calls ```choosing_information()```, ```printing_or_navigating()``` and one of ```navigate_list()``` or ```navigate_dictionary()``` functions. This function is also in the ```while True``` cycle so that it is recursive
```python
def navigate_dictionary(data):
    while True:
        ...

        user_choice = choosing_information(show_possible_choices)
        ...

        if type(chosen_info) == dict:
            value = printing_or_navigating(chosen_info)
            ...

        elif type(chosen_info) == list:
            value = printing_or_navigating(chosen_info)
            ...
```
## main()
The main function that connects the program together, transfering the data from one function to another
```python
def main():
    path_to_file = input("Enter a " + colored("file name", "green", attrs=['bold']) + " to be explored:\n" +
                         colored(">>> ", "red", attrs=['bold']))
    data = read_json_file(path_to_file)
    user_post = choosing_post(data)
    if type(user_post) == dict:
        navigate_dictionary(user_post)
    else:
        navigate_list(user_post)
```

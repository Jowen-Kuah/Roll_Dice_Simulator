import random

def validate_menu(user_input):
    if len(user_input) == 0:
        print("Presence Check Failed!")
        return False
    elif not user_input.isdigit():
        print("Type Check Failed!")
        return False
    elif int(user_input) < 1 or int(user_input) > 2:
        print("Range Check Failed")
        return False
    else:
        return True
    
def validate_input(msg):
    done = False
    while not done:
        home_screen()
        user_input = input(msg)
        done = validate_menu(user_input)
    return user_input
    
def home_screen():
    display = """
    1. Roll the dice
    2. Quit
    """
    print(display)
def user_menu():
    done = False
    while not done:
        user_input = validate_input(msg = "Please select an option: ")
        if user_input == '1':
            result = random.randint(1, 6)
            print(result)
        else:
            done = True
            print("Goodbye!")
user_menu()

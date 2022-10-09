import typing




def get_option_number(start_range: int=1, end_range: int=6, ) -> int:
    """
    Get option selected by user
    :param start_range: Smallest number that can be selected by user. Typically first menu option #.
    :param end_range:   Largest number than can be selected by user. Typically last menu option.
    :return:            number/option selected by user. If quit allowed, -1 signifies user wants to quit.
    """
    invalid_input = True
    while invalid_input:
        try:
            choice = input("Please enter you option selection: ")
            not_a_number = not choice.isdigit()
            if not_a_number:
                choice = -1
                invalid_input = False
            elif int(choice) < start_range or int(choice) > end_range:
                print("\nInvalid input. Please try again.\n")
                invalid_input = True
            else:
                choice = int(choice)
                invalid_input = False
        except Exception:
            print("\nUnable to process input. Please try again.\n")

    return choice

def show_ingredient_change_menu() -> None:
    """
        Presents ingredient change menu to user.
        :return: prints to console several menu choices
        """
    print()
    print("1 - Add an ingredient")
    print("2 - Edit/Change an ingredient")
    print("3 - Delete an ingredient")
    print("B - Return to previous screen. Any non-numeric key accepted\n")

def show_recipe_change_menu() -> None:
    """
        Presents recipe change menu to user.
        :return: prints to console several menu choices
        """
    print()
    print("1 - Add a recipe")
    print("2 - Edit/Change a recipe")
    print("3 - Delete an recipe")
    print("B - Return to previous screen. Any non-numeric key accepted\n")

def show_main_menu(product_name: str) -> None:
    """
    Presents starting menu to user.
    :param product_name - name of recipe application
    :return: prints to console several menu choices
    """
    print("\nWelcome to " + str(product_name) + ".")
    print("1 - Learn a new recipe")
    print("2 - Find best recipe given ingredients you have")
    print("3 - View all recipes")
    print("4 - View all ingredients")
    print("5 - Add/Edit/Update/Delete a recipe")
    print("6 - Add/Edit/Update/Delete an ingredient")
    print("Q - Quit the program. Any non-numeric key accepted\n")
# Author:
# GitHub username:
# Date:
# Description:
import os.path
import typing

import Recipe
import Ingredient
import menu


def closing_procedures():
    pass


def add_ingrediant(container: list) -> None:
    name = input("Enter ingredient name: ")
    ingredient_id = input("Enter ingredient id#: ")
    item = Ingredient.Ingredient(ingredient_id, name)
    # need to add ingredient to ingredients
    # check if name already used
    container.append(item)
    filename = "ingredients.txt"
    try:
        with open(filename, "a") as document:
            #Note: append mode will create file if not exists
            document.write(str(ingredient_id) + "," + str(name) + "\n")
    except Exception:
        print("Unable to update ingredients file. Please contact IT so data can be retained after session ends")


def main():

    ingredients = []
    menu.show_main_menu("RecipeFinder")
    selection = menu.get_option_number(1, 6)
    QUIT_OPTION_VALUE = -1

    while selection != QUIT_OPTION_VALUE:
        if selection == 1:
            pass
        elif selection == 2:
            pass
        elif selection == 3:
            pass
        elif selection == 4:
            pass
        elif selection == 5:
            pass
        elif selection == 6:
            # theoretically show all ingredients then menu
            menu.show_ingredient_change_menu()
            ingredient_option = menu.get_option_number(1, 3)
            ADD_INGREDIENT_OPTION_VALUE, EDIT_MODE = 1, 2

            if ingredient_option == ADD_INGREDIENT_OPTION_VALUE:
                add_ingrediant(ingredients)
            elif ingredient_option == EDIT_MODE:
                pass
            else:
                # DELETE INGREDIENT
                pass
        else:
            closing_procedures()

        menu.show_main_menu("RecipeFinder")
        selection = menu.get_option_number(1, 6)


if __name__ == "__main__":
    main()
    #test






def create_log():
    pass

def generate_random_number():
    pass





def add_recipe():
    pass

def get_best_match():
    pass

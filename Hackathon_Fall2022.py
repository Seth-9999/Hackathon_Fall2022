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


def add_recipe(container: list) -> None:
    name = input("Enter recipe name: ")
    recipe_id = input("Enter recipe id#: ")

    # allow 0 cooking time b/c non-cooking stuff
    cooking_time_minutes = -1
    while cooking_time_minutes < 0:
        try:
            cooking_time_minutes = int(input("Enter cooking time (in minutes, positive integers only): "))
        except Exception:
            print("\nPlease enter a valid number. Unable to convert to positive integer >= 0.\n")

    item = Recipe.Recipe(recipe_id, name, cooking_time_minutes)
    # need to add recipe to recipes
    # check if name already used
    container.append(item)
    filename = "recipes.txt"
    try:
        file_already_exists =  True if os.path.exists(filename) else False
        with open(filename, "a") as document:
            #Note: append mode will create file if not exists
            if file_already_exists:
                document.write("\n")
            document.write(str(recipe_id) + "," + str(name) + "," + str(cooking_time_minutes))
    except Exception:
        print("Unable to update recipes file. Please contact IT so data can be retained after session ends")


def load_recipes(some_list):
    # check for file?
    filename = "recipes.txt"
    with open(filename, "r") as filein:
        for line in filein:
            line = line.strip()
            temp = line.split(",")
            some_id = temp[0]
            some_name = temp[1]
            item = Ingredient.Ingredient(some_id, some_name)
            some_list.append(item)
    print(some_list[3])


def load_ingredients(some_list):
    # check for file?
    filename = "ingredients.txt"
    with open(filename, "r") as filein:
        for line in filein:
            line = line.strip()
            temp = line.split(",")
            some_id = temp[0]
            some_name = temp[1]
            item = Ingredient.Ingredient(some_id, some_name)
            some_list.append(item)


def populate_recipies_by_ingred(hashmap, ingredients, recipies):
    # check for file?
    filename = "junctiontable.txt"
    with open(filename, "r") as filein:
        for line in filein:

            line = line.strip()
            temp = line.split(",")
            recipe_id = temp[0]
            ingredient_id = temp[1]

            if ingredient_id in hashmap:
                a_list = hashmap[ingredient_id]
                a_list.append(recipe_id)
            else:
                temp = [recipe_id]
                hashmap[ingredient_id] = temp


def startup_procedures(ingredients_list, recipes_list, dict_recipies_by_ingredients):
    load_ingredients(ingredients_list)
    load_recipes(recipes_list)
    populate_recipies_by_ingred(dict_recipies_by_ingredients, ingredients_list, recipes_list)
    temp = 5

def main():
    ingredients = []
    recipes = []
    recipes_by_ingredients = {}
    startup_procedures(ingredients, recipes,recipes_by_ingredients)
    menu.show_main_menu("RecipeFinder")
    selection = menu.get_option_number(1, 6)
    QUIT_OPTION_VALUE = -1
    INGREDIENT_OPTION, RECIPE_OPTION = 6, 5
    while selection != QUIT_OPTION_VALUE:
        if selection == 1:
            pass
        elif selection == 2:
            pass
        elif selection == 3:
            pass
        elif selection == 4:
            pass
        elif selection == RECIPE_OPTION:
            menu.show_recipe_change_menu()
            recipe_option = menu.get_option_number(1, 3)
            ADD_RECIPE_OPTION_VALUE, RECIPE_EDIT_MODE = 1, 2
            if recipe_option == ADD_RECIPE_OPTION_VALUE:
                add_recipe(recipes)
            elif recipe_option == RECIPE_EDIT_MODE:
                pass
            else:
                # DELETE INGREDIENT
                pass
        elif selection == INGREDIENT_OPTION:
            # theoretically show all ingredients then menu
            menu.show_ingredient_change_menu()
            ingredient_option = menu.get_option_number(1, 3)
            ADD_INGREDIENT_OPTION_VALUE, INGREDIENT_EDIT_MODE = 1, 2

            if ingredient_option == ADD_INGREDIENT_OPTION_VALUE:
                add_ingrediant(ingredients)
            elif ingredient_option == INGREDIENT_EDIT_MODE:
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

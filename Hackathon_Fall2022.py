"""
Name:「 RECIPE FINDER」
Description: Ask the user to enter the ingredients they have and give them the best fit of the recipe.
"""


def main():
    show_the_ingredients()
    add_recipe()
    number = input("How many ingredients do you want to add? ")
    # only number is the legal format
    while number.isalpha():
        print("Error! Please a number.")
        number = input("How many ingredients do you want to add? ")
    get_the_best_fit(number)


def show_the_ingredients():
    print("**************************** Cooking Ingredients *****************************")
    print("| Avocado   = 01  | Bread           = 02  | Bacon     = 03  | Butter    = 04 |")
    print("| Chives    = 05  | Cheese          = 06  | Eggs      = 07  | Fruit     = 08 |")
    print("| Garlic    = 09  | Honey           = 10  | Milk      = 11  | Olive oil = 12 |")
    print("| Onion     = 13  | Potatoes        = 14  | Parshnips = 15  | Spinach   = 16 |")
    print("| Sausage   = 17  | Salt and Pepper = 18  | Tortillas = 19  | Yogurt    = 20 |")
    print("******************************************************************************")


# create the recipe file
def add_recipe():
    path = 'Mashed Parsnips.txt'
    with open(path, 'w+') as f:
        lines = ['14, Potatoes\n', '15, Parshnips\n', '18, Salt and Pepper\n', '11, Milk\n', '04, Butter\n',
                 '09, Garlic\n', '05, Chives\n']
        f.writelines(lines)
    path = 'Roasted Potato and Chorizo Hash.txt'
    with open(path, 'w+') as f:
        lines = ['13, Onion\n', '14, Potatoes\n', '18, Salt and Pepper\n', '09, Garlic\n', '12, Olive oil\n',
                 '07, Eggs\n', '06, Cheese\n', '19, Tortillas\n']
        f.writelines(lines)
    path = 'Sausage and Egg Sandwiches.txt'
    with open(path, 'w+') as f:
        lines = ['12, Olive oil\n', '13, Onion\n', '17, Sausage\n', '06, Cheese\n', '07, Eggs\n', '02, Bread\n',
                 '18, Salt and Pepper\n']
        f.writelines(lines)


def choose_ingredients():
    print("What cooking ingredients do you have?")
    ingredients = input("Enter a number: ")
    # define the legal format of input
    while ingredients.isalpha() or len(ingredients) < 2 or len(ingredients) > 2 or int(ingredients) > 20:
        print("Error! Please reenter completely the correct number from 01 to 20!")
        ingredients = input("Enter a number: ")
    return ingredients


def check_ingredients(ingredients, filename):
    count = 0
    # find the match ingredients from each recipe based on the user input
    with open(filename) as f:
        if ingredients in f.read():
            count += 1
        return count


def get_the_best_fit(number):
    match_1 = 0
    match_2 = 0
    match_3 = 0
    num = int(number)
    # the loop is depended on how many ingredients the user want to add
    for i in range(num):
        ingredients = choose_ingredients()
        # count how many matching ingredients respectively
        count_1 = check_ingredients(ingredients, "Mashed Parsnips.txt")
        if count_1 == 1:
            match_1 += count_1
        count_2 = check_ingredients(ingredients, "Roasted Potato and Chorizo Hash.txt")
        if count_2 == 1:
            match_2 += count_2
        count_3 = check_ingredients(ingredients, "Sausage and Egg Sandwiches.txt")
        if count_3 == 1:
            match_3 += count_3
    print("======================================== Your Result ========================================")
    # compare the value and find the highest matching recipe
    if match_1 > match_2 >= match_3 or match_1 > match_3 >= match_2:
        print("The 'Mashed Parsnips' recipe is the best fit because you have", match_1, "ingredients.")
        show_the_recipe("Mashed Parsnips.txt")
    elif match_2 > match_1 >= match_3 or match_2 > match_3 >= match_1:
        print("The 'Roasted Potato and Chorizo Hash' recipe is the best fit because you have", match_2, "ingredients.")
        show_the_recipe("Roasted Potato and Chorizo Hash.txt")
    elif match_3 > match_1 >= match_2 or match_3 > match_2 >= match_1:
        print("The 'Sausage and Egg Sandwiches' recipe is the best fit because you have", match_3, "ingredients.")
        show_the_recipe("Sausage and Egg Sandwiches.txt")
    else:
        print("There is no best fit recipe for you :(")


def show_the_recipe(filename):
    with open(filename, 'r') as f:
        print(f.read())


if __name__ == "__main__":
    main()

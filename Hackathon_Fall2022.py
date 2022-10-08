# Author:
# GitHub username:
# Date:
# Description:


def main():
    show_the_ingredients()
    add_recipe()
    num = int(input("How many ingredients do you want to add? "))
    match_1 = 0
    match_2 = 0
    for i in range(num):
        ingredients = choose_ingredients()
        count_1 = check_ingredients_1(ingredients)
        if count_1 == 1:
            match_1 += count_1
        count_2 = check_ingredients_2(ingredients)
        if count_2 == 1:
            match_2 += count_2
    if match_1 > match_2:
        print("The 'Mashed Parsnips' is the best fit because you have", match_1, "ingredients of it.")
    else:
        print("The 'Roasted Potato and Chorizo Hash' is the best fit because you have", match_2, "ingredients of it.")


def show_the_ingredients():
    print("*************************** Cooking Ingredients ****************************")
    print("| Avocado   = 01 | Bread           = 02 | Bacon     = 03  | Butter    = 04 |")
    print("| Chives    = 05 | Cheese          = 06 | Eggs      = 07  | Fruit     = 08 |")
    print("| Garlic    = 09 | Honey           = 10 | Milk      = 11  | Olive oil = 12 |")
    print("| Onion     = 13 | Potatoes        = 14 | Radish    = 15  | Spinach   = 16 |")
    print("| Sausage   = 17 | Salt and Pepper = 18 | Tortillas = 19  | Yogurt    = 20 |")
    print("| Parshnips = 21 | Chives          = 22 |           = 23  |           = 24 |")
    print("****************************************************************************")


def add_recipe():
    path = 'Mashed Parsnips.txt'
    with open(path, 'w+') as f:
        lines = ['14, Potatoes\n', '21, Parshnips\n', '18, Salt and Pepper\n', '11, Milk\n', '04, Butter\n',
                 '09, Garlic\n', '22, Chives\n']
        f.writelines(lines)
    path = 'Roasted Potato and Chorizo Hash.txt'
    with open(path, 'w+') as f:
        lines = ['13, Onion\n', '14, Potatoes\n', '18, Salt and Pepper\n', '09, Garlic\n', '12, Olive oil\n',
                 '07, Eggs\n', '06, Cheese\n', '19, Tortillas\n']
        f.writelines(lines)


def choose_ingredients():
    print("What cooking ingredients do you have?")
    ingredients = input("Enter the abbreviation: ")
    return ingredients


def check_ingredients_1(ingredients):
    count_1 = 0
    with open('Mashed Parsnips.txt') as f:
        if ingredients in f.read():
            count_1 += 1
        return count_1


def check_ingredients_2(ingredients):
    count_2 = 0
    with open('Roasted Potato and Chorizo Hash.txt') as f:
        if ingredients in f.read():
            count_2 += 1
        return count_2


if __name__ == "__main__":
    main()


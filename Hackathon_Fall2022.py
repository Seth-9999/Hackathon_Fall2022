# Author:
# GitHub username:
# Date:
# Description:


def main():
    show_the_ingredients()
    add_recipe()
    num = int(input("How many ingredients do you want to add? "))
    match = 0
    for i in range(num):
        ingredients = choose_ingredients()
        count = check_ingredients(ingredients)
        match += count
    print(match)


def show_the_ingredients():
    print("*************************** Cooking Ingredients ***************************")
    print("| Avocado   = A  | Bread           = B  | Bacon     = BA | Butter    = BU |")
    print("| Chives    = CH | Cheese          = CS | Eggs      = E  | Fruit     = F  |")
    print("| Garlic    = G  | Honey           = H  | Milk      = M  | Olive oil = O  |")
    print("| Onion     = ON | Potatoes        = PO | Radish    = R  | Spinach   = S  |")
    print("| Sausage   = SA | Salt and Pepper = SP | Tortillas = T  | Yogurt    = Y  |")
    print("***************************************************************************")


def add_recipe():
    path = 'Mashed Parsnips.txt'
    with open(path, 'w+') as f:
        lines = ['Potatoes\n', 'Parshnips\n', 'Salt and Pepper\n', 'Milk\n', 'Butter\n', 'Garlic\n', 'Chives\n']
        f.writelines(lines)
    path = 'Roasted Potato and Chorizo Hash.txt'
    with open(path, 'w+') as f:
        lines = ['Onion\n', 'Potatoes\n', 'Salt and Pepper\n', 'Garlic\n', 'Olive oil\n', 'Eggs\n', 'Cheese\n',
                 'Tortillas\n']
        f.writelines(lines)


def choose_ingredients():
    print("What cooking ingredients do you have?")
    ingredients = input("Enter the abbreviation: ")
    return ingredients


def check_ingredients(ingredients):
    count = 0
    with open('Mashed Parsnips.txt') as f:
        if ingredients in f.read():
            count += 1
        return count


if __name__ == "__main__":
    main()


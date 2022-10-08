# Author:
# GitHub username:
# Date:
# Description:


class Recipe:

    def __init__(self, id, name, cooking_time=0):
        self._id = id
        self._name = name
        self._cooking_time = cooking_time

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def get_cooking_time(self):
        return self._cooking_time


class Ingredient:

    def __init__(self, id, name):
        self._id = id
        self._name = name

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name



def add_recipe():
    pass



def add_ingrediant():
    pass

def main():
    print("Success")
    choices = input("Enter ingredient")
    pass

def create_log():
    pass

def generate_random_number():
    pass

def get_best_match():
    pass

if __name__ == "__main__":
    main()
    #test




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





def add_recipe():
    pass

def get_best_match():
    pass

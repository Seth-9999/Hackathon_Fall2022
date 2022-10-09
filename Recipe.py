
class Recipe:
    """Example: Apple Pie  """

    def __init__(self, id: str, name: str, cooking_time_in_minutes: int = 0) -> None:
        """param cooking_time: Integer. How many minutes required to cook food involved in recipe"""
        self._id = str(id)
        self._name = name
        self._cooking_time = int(cooking_time_in_minutes)
        self._components = None

    def set_name(self, name: str) -> None:
        """
        Renaming a receipe. Example: Apple Pie can be renamed as Apple Pumpkin Pie.
        :param name: new name for the Recipe.
        :return: None
        """
        self._name = name

    def get_name(self) -> str:
        """
        Return name of the recipe
        :return: name of the recipe
        """
        return self._name

    def get_cooking_time(self) -> int:
        """
        Returns cooking time for a recipe
        :return: number of minutes that will be spent cooking when preparing this recipe
        """
        return self._cooking_time

    def get_components(self):
        # do I need to worry about returning same instance vs duplicate
        return self._components

    def set_one_component(self, ingredient_id):
        if self._components is None:
            self._components = []
        self._components.append(ingredient_id)

    def set_multiple_component(self, some_list):
        # some_list has to be an iterable like list, set, tuple
        if self._components is None:
            self._components = some_list
        else:
            self._components.extend(some_list)





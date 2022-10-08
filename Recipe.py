
class Recipe:
    """Example: Apple Pie  """

    def __init__(self, id: str, name: str, cooking_time_in_minutes: int = 0) -> None:
        """param cooking_time: Integer. How many minutes required to cook food involved in recipe"""
        self._id = str(id)
        self._name = name
        self._cooking_time = int(cooking_time_in_minutes)

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





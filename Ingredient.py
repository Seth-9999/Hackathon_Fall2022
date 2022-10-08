
class Ingredient:
    """Components used to make food recipes like olive oil, chicken, oregeno, etc"""

    def __init__(self, ingredient_id: str, name: str) -> None:
        self._id = str(ingredient_id)
        self._name = name

    def set_name(self, name: str) -> None:
        """
        Re-naming an ingredient
        :param name - Set/change the name of an ingredient.
        :return None
        """
        self._name = name

    def get_name(self) -> str:
        """
        Returns the name of the ingredient
        :return Name of the ingredient
        """
        return self._name

    def get_id(self) -> str:
        """
        Return id# for ingredient
        :param self: NA
        :return: String. id# of the ingredient
        """
        return self._id




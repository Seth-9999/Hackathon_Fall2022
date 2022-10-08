
class Ingredient:
    """Components used to make food like olive oil, chicken, oregeno, etc"""

    def __init__(self, id: str , name: str) -> None:
        self._id = str(id)
        self._name = name

    def set_name(self, name: str) -> None:
        """
        Change name of the ingredient
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

    def __get_id(self) -> str:
        """
        (Private) helper method for testing purposes,etc
        :param self: NA
        :return: String. id# of the ingredient
        """
        return self._id




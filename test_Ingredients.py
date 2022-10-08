import unittest
import Ingredient

class MyTestCase(unittest.TestCase):
    def test_ingredient_initialization(self):
        # tests get name, get id, and initialization
        actual_name = "SomeIngredient"
        actual_id = "I01"
        item = Ingredient.Ingredient(actual_id, actual_name)
        name_retrieved = item.get_name()
        id_retrieved = item.get_id()
        self.assertEqual(actual_id, id_retrieved)  # add assertion here
        self.assertEqual(actual_name, name_retrieved)

    def test_set_name(self):
        item = Ingredient.Ingredient("SomeIngred", "I01")
        actual_name = "FakeName"
        item.set_name(actual_name)
        name_retrieved = item.get_name()
        self.assertEqual(actual_name, name_retrieved)



if __name__ == '__main__':
    unittest.main()

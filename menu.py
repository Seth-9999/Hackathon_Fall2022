import typing


class MainMenu:
    """Option menu for """



    def get_option_number(allow_quit: typing.Any, start_range: int=1, end_range: int=6, ) -> int:
        """
        Get option selected by user
        :param start_range: Smallest number that can be selected by user. Typically first menu option #.
        :param end_range:   Largest number than can be selected by user. Typically last menu option.
        :param allow_quit:  can user enter specific command to quit option selection and application itself.
        :return:            number/option selected by user. If quit allowed, -1 signifies user wants to quit.
        """
        invalid_input = True
        while invalid_input:
            try:
                choice = input("Please enter you option selection: ")
                not_a_number = not choice.isdigit()
                if not_a_number:
                    choice = -1
                    invalid_input = False
                elif int(choice) < start_range or int(choice) > end_range:
                    print("\nInvalid input. Please try again.\n")
                    invalid_input = True
                else:
                    choice = int(choice)
                    invalid_input = False
            except Exception:
                print("\nUnable to process input. Please try again.\n")

        return choice

    def show_main_menu(productName: str) -> None:
        """
        Presents menu to user.
        :param productName - name of this product
        :return: prints to console several menu choices
        """
        print("\nWelcome to " + str(productName) + ".")
        print("1 - Learn a new recipe")
        print("2 - Find best recipe given ingredients you have")
        print("3 - View all recipes")
        print("4 - View all ingredients")
        print("5 - Edit/Update/Delete a recipe")
        print("6 - Edit/Update/Delete an ingredient")
        print("Q - Quit the program. Any non-numeric key accepted\n")
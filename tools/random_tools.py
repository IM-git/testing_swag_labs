import random


class RandomTools:
    """
    Various methods for obtaining different
    values are presented here.
    """

    class RandomValue:
        """Getting random value."""

        @staticmethod
        def get_random_number(initial_value: int, end_value: int) -> int:
            return random.randint(initial_value, end_value)

        @staticmethod
        def get_random_value_from_sequence(values):
            """This can be sequence of an any type."""
            quantity = len(values) - 1
            num = random.randint(0, quantity)
            return values[num]

        @staticmethod
        def get_random_name_from_dictionary(values):
            gender = random.choice(list(values.keys()))
            name = random.choice(values[gender])
            return name


if __name__ == '__main__':
    list_name = ['Abigail', 'Ava', 'Airi', 'Alexa', 'Alexandra', 'Alexis',
                 'Alice', 'Alia', 'Amelia', 'Amia', 'Angelina', 'Anna',
                 'Ariana', 'Briana', 'Brooke']
    dict_names = {"girls": ["Abigail", "Ava", "Airi", "Alexa", "Alexandra"],
                  "boys": ["Adam", "Aaron", "Adrian", "Aidan", "Alex"]
                  }
    print(RandomTools.RandomValue.get_random_value_from_sequence(list_name))
    print(RandomTools.RandomValue.get_random_name_from_dictionary(dict_names))

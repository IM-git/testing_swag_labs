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

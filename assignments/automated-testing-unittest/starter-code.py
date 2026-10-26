import unittest


def add_numbers(first, second):
    return first + second


def is_even(number):
    return number % 2 == 0


def normalize_name(value):
    return " ".join(value.split()).title()


class TestUtilityFunctions(unittest.TestCase):
    def test_add_numbers(self):
        # Check the result of adding two numbers.
        pass

    def test_is_even(self):
        # Check both even and odd numbers.
        pass

    def test_normalize_name(self):
        # Check leading, trailing, and repeated whitespace.
        pass


if __name__ == "__main__":
    unittest.main()

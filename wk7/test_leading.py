import unittest
# need to put code in .py file so we can import it like this
from leading import *

class Testing_leading_substrings(unittest.TestCase):
    """ Tests for leading_substrings"""

    def test_leading_substrings_empty(self):
        """ Test a string with just one character."""
        inputted = ""
        output = leading_substrings(inputted)
        output_expected = []
        self.assertEqual(output_expected, output, "The string is empty.")

    def test_leading_substrings_one(self):
        """ Test a string with just one character."""
        inputted = "a"
        output = leading_substrings(inputted)
        output_expected = ["a"]
        self.assertEqual(output_expected, output, "The string has one character")

    def test_leading_substrings_two_words(self):
        """ Test a string with just one character."""
        inputted = "Hello World"
        output = leading_substrings(inputted)
        output_expected = ["H", "He", "Hel", "Hell", "Hello", "Hello ", "Hello W", "Hello Wo", "Hello Wor", "Hello Worl", "Hello World"]
        self.assertEqual(output_expected, output, "The string consists of two words (in one string)")
    
    def test_leading_substrings_two_separate_words(self):
        """ Test a string with just one character."""
        inputted = "Hello" "World"
        output = leading_substrings(inputted)
        output_expected = ["H", "He", "Hel", "Hell", "Hello", "Hello ", "Hello W", "Hello Wo", "Hello Wor", "Hello Worl", "Hello World"]
        self.assertEqual(output_expected, output, "The string consists of two separate words")    

if __name__ == '__main__': 
    unittest.main()
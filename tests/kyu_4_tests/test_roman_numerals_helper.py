import unittest

from katas.kyu_4.roman_numerals_helper import RomanNumerals


class RomanNumeralsHelperTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(RomanNumerals.to_roman(1000), 'M')

    def test_equals_2(self):
        self.assertEqual(RomanNumerals.from_roman('M'), 1000)

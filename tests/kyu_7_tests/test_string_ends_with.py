import unittest

from katas.kyu_7.string_ends_with import solution


class StringEndsWithTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(solution('abc', 'bc'))

    def test_false(self):
        self.assertFalse(solution('abc', 'd'))

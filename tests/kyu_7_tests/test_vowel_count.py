import unittest

from katas.kyu_7.vowel_count import getCount


class GetCountTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(getCount('abracadabra'), 5)

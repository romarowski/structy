import unittest as ut
from string_array.greatest_common_divisor_of_strings import gcdOfStrings


class TestGCDOfStrings(ut.TestCase):
    def test_common_divisor_exists(self):
        str1 = "ABCABC"
        str2 = "ABC"
        expected_output = "ABC"
        self.assertEqual(gcdOfStrings(str1, str2), expected_output)

    def test_no_common_divisor(self):
        str1 = "ABABAB"
        str2 = "CD"
        expected_output = ""
        self.assertEqual(gcdOfStrings(str1, str2), expected_output)

    def test_empty_strings(self):
        str1 = ""
        str2 = ""
        expected_output = ""
        self.assertEqual(gcdOfStrings(str1, str2), expected_output)

    def test_same_string(self):
        str1 = "XYZ"
        str2 = "XYZ"
        expected_output = "XYZ"
        self.assertEqual(gcdOfStrings(str1, str2), expected_output)

    def test_long_string(self):
        str1 = "TAUXX" * 5
        str2 = "TAUXX" * 9 
        expected_output = "TAUXX"
        self.assertEqual(gcdOfStrings(str1, str2), expected_output)


    def test_more_strings(self):
        str1 = "AAAAAAAAA"
        str2 = "AAACCC"
        expected_output = ""
        self.assertEqual(gcdOfStrings(str1, str2), expected_output)
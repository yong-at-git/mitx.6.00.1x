from unittest import TestCase
import sum_digits as sd


class TestSumDigits(TestCase):
    def test_sum_digits_all_digits(self):
        s = '12345'
        expected = 15
        actual = sd.sum_digits(s)
        self.assertEqual(expected, actual)

    def test_sum_digits_no_digits(self):
        s = 'abc'
        with self.assertRaises(ValueError):
            sd.sum_digits(s)

    def test_sum_digits_empty(self):
        s = ''
        with self.assertRaises(ValueError):
            sd.sum_digits(s)

    def test_sum_digits_digit_and_char(self):
        s = '12a34.5*'
        expected = 15
        actual = sd.sum_digits(s)
        self.assertEqual(expected, actual)

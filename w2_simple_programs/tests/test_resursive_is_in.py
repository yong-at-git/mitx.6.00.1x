from unittest import TestCase
from recursive_check_char_in_str import *


class TestIs_in(TestCase):
    def test_is_in_1(self):
        self.assertFalse(is_in('a', ''))

    def test_is_in_2(self):
        self.assertFalse(is_in('u', 'cddfhijjllmnqqqrss'))

    def test_is_in_3(self):
        self.assertFalse(is_in('b', 'dejlmnprtv'))

    def test_is_in_4(self):
        self.assertFalse(is_in('v', 'abdeeghiwwxz'))

    def test_is_in_5(self):
        self.assertFalse(is_in('w', 'l'))

    def test_is_in_6(self):
        self.assertFalse(is_in('y', 'abcdhjjklnqrwxz'))

    def test_is_in_7(self):
        self.assertTrue('j', 'j')

    def test_is_in_8(self):
        self.assertTrue('n', 'aabdjjnppstvwwyy')

    def test_is_in_9(self):
        self.assertTrue('u', 'ou')

    def test_is_in_10(self):
        self.assertTrue('a', 'akm')

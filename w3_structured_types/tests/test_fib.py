from unittest import TestCase
from fib import fib_with_dict, naive_fib


class TestFib(TestCase):
    def test_naive_fib_1(self):
        self.assertEqual(1, naive_fib(1))

    def test_fib_with_dict_1(self):
        a_dict = {1: 1, 2: 1}
        self.assertEqual(1, fib_with_dict(1, a_dict))

    def test_naive_fib_2(self):
        self.assertEqual(1, naive_fib(2))

    def test_fib_with_dict_2(self):
        a_dict = {1: 1, 2: 1}
        self.assertEqual(1, fib_with_dict(2, a_dict))

    def test_naive_fib_3(self):
        self.assertEqual(2, naive_fib(3))

    def test_fib_with_dict_3(self):
        a_dict = {1: 1, 2: 1}
        self.assertEqual(2, fib_with_dict(3, a_dict))

    def test_naive_fib_4(self):
        self.assertEqual(3, naive_fib(4))

    def test_fib_with_dict_4(self):
        a_dict = {1: 1, 2: 1}
        self.assertEqual(3, fib_with_dict(4, a_dict))

    def test_naive_fib_4(self):
        self.assertEqual(610, naive_fib(15))

    def test_fib_with_dict_4(self):
        a_dict = {1: 1, 2: 1}
        self.assertEqual(610, fib_with_dict(15, a_dict))
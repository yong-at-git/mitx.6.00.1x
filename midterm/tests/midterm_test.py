from unittest import TestCase
import midterm_solution


class TestMidTerm(TestCase):
    def test_is_triangular_true(self):
        for i in (1, 3, 6, 10, 15, 21, 28, 36, 45):
            self.assertTrue(midterm_solution.is_triangular(i))

    def test_is_triangular_false(self):
        for i in (2, 4, 7, 11, 16, 22, 29, 37, 46):
            self.assertFalse(midterm_solution.is_triangular(i))

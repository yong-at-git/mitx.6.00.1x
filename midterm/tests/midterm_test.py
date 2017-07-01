from unittest import TestCase
import midterm_solution


class TestMidTerm(TestCase):
    def test_is_triangular_true(self):
        for i in (1, 3, 6, 10, 15, 21, 28, 36, 45):
            self.assertTrue(midterm_solution.is_triangular(i))

    def test_is_triangular_false(self):
        for i in (2, 4, 7, 11, 16, 22, 29, 37, 46):
            self.assertFalse(midterm_solution.is_triangular(i))

    def test_print_without_vowels_1(self):
        s = "This is great!"
        expected = "Ths s grt!"
        self.assertEqual(expected, midterm_solution.print_without_vowels(s))

    def test_print_without_vowels_2(self):
        s = "a"
        expected = ""
        self.assertEqual(expected, midterm_solution.print_without_vowels(s))

    def test_print_without_vowels_case_sensitive_1(self):
        s = "aNd, nOW! I'm --so-- t35t1n@ those special chars!!"
        expected = "Nd, nW! 'm --s-- t35t1n@ ths spcl chrs!!"
        self.assertEqual(expected, midterm_solution.print_without_vowels(s))

    def test_print_without_vowels_case_sensitive_2(self):
        s = "Here is a simple sentence that makes sense. BYE."
        expected = "Hr s  smpl sntnc tht mks sns. BY."
        self.assertEqual(expected, midterm_solution.print_without_vowels(s))
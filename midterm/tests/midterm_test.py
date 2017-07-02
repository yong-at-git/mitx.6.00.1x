from unittest import TestCase
import midterm_solution


class TestMidTerm(TestCase):
    ##
    # test is_triangular
    ##
    def test_is_triangular_true(self):
        for i in (1, 3, 6, 10, 15, 21, 28, 36, 45):
            self.assertTrue(midterm_solution.is_triangular(i))

    def test_is_triangular_false(self):
        for i in (2, 4, 7, 11, 16, 22, 29, 37, 46):
            self.assertFalse(midterm_solution.is_triangular(i))

    ##
    # test print_without_vowels
    ##
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

    #
    # test largest_odd_times
    #
    def test_largest_odd_times_1(self):
        self.assertIsNone(midterm_solution.largest_odd_times([2, 2, 4, 4]))

    def test_largest_odd_times_2(self):
        self.assertEqual(9, midterm_solution.largest_odd_times([3, 9, 5, 3, 5, 3]))

    def test_largest_odd_times_3(self):
        self.assertEqual(4, midterm_solution.largest_odd_times([2, 4, 5, 4, 5, 4, 2, 2]))

    def test_largest_odd_times_4(self):
        self.assertEqual(3, midterm_solution.largest_odd_times([3, 0, 5, 3, 5, 3]))

    def test_largest_odd_times_5(self):
        self.assertEqual(2, midterm_solution.largest_odd_times([3, 3, 2, 0]))

    #
    # test dict_invert
    #
    def test_dict_invert_1(self):
        dict = {1: 10, 2: 20, 3: 30}
        expected = {10: [1], 20: [2], 30: [3]}
        self.assertEqual(expected, midterm_solution.dict_invert(dict))

    def test_dict_invert_2(self):
        dict = {1: 10, 2: 20, 3: 30, 4: 30}
        expected = {10: [1], 20: [2], 30: [3, 4]}
        self.assertEqual(expected, midterm_solution.dict_invert(dict))

    def test_dict_invert_3(self):
        dict = {4: True, 2: True, 0: True}
        expected = {True: [0, 2, 4]}
        self.assertEqual(expected, midterm_solution.dict_invert(dict))

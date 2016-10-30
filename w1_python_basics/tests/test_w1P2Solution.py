from unittest import TestCase
from solution.p2_sub_str_count import W1P2Solution


class TestW1P2Solution(TestCase):
    def test_count_sub_str_occurrence(self):
        self.assertEqual(W1P2Solution.count_sub_str_occurrence('exxbobbobboobboobgboboboboobosqcup'), 5)
        self.assertEqual(W1P2Solution.count_sub_str_occurrence('rmobootvqh'), 0)
        self.assertEqual(W1P2Solution.count_sub_str_occurrence('aoboboboobbobbjbobobbobobeobobtbobbobooboobf'
                                                               ), 10)

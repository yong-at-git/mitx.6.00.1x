from unittest import TestCase
from solution.p1_vowel_counting import W1P1Solution


class TestW1P1Solution(TestCase):
    def test_count_vowel(self):
        s = 'azcbobobegghakl'
        expected_num = 5
        self.assertEqual(W1P1Solution.count_vowel(s), expected_num)

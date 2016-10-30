from unittest import TestCase
from solution.p3_longest_ordered_sub_str import W1P3Solution


class TestW1P3Solution(TestCase):
    def test_get_longest_ordered_sub_str(self):
        self.assertEqual('afs', W1P3Solution.get_longest_ordered_sub_str('qdafsljwkxbbxgmgko'))
        self.assertEqual('dkz', W1P3Solution.get_longest_ordered_sub_str('dkzelvnqqeareuqo'))
        self.assertEqual('abcdefghijklmnopqrstuvwxyz',
                         W1P3Solution.get_longest_ordered_sub_str('abcdefghijklmnopqrstuvwxyz'))
        self.assertEqual('txx', W1P3Solution.get_longest_ordered_sub_str('txxlxicbzku'))

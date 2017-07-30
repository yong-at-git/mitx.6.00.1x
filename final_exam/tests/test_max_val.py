from unittest import TestCase
import max_val as mv


class TestMax_val(TestCase):
    def test_max_val_1(self):
        in_ds = (5, (1, 2), [[1], [2]])
        expected = 5
        actual = mv.max_val(in_ds)
        self.assertEqual(expected, actual)

    def test_max_val_1(self):
        in_ds = (5, (1, 2), [[1], [9]])
        expected = 9
        actual = mv.max_val(in_ds)
        self.assertEqual(expected, actual)

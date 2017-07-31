from unittest import TestCase
import Bag


class TestASet(TestCase):
    def test_remove(self):
        d1 = Bag.ASet()
        d1.insert(4)
        d1.insert(4)

        d1.remove(2)
        self.assertTrue('4:2' in d1.__str__())

        d1.remove(4)
        self.assertEqual('', d1.__str__())

    def test_is_in(self):
        d1 = Bag.ASet()
        d1.insert(4)
        self.assertTrue(d1.is_in(4))

        d1.insert(5)
        self.assertTrue(d1.is_in(5))

        d1.remove(5)
        self.assertFalse(d1.is_in(5))

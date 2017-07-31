from unittest import TestCase
import Bag


class TestBag(TestCase):
    def test_remove(self):
        bag = Bag.Bag()
        bag.insert(4)
        bag.insert(4)
        bag_str = bag.__str__()
        self.assertEqual('4:2\n', bag_str)

        bag.remove(2)
        bag_str = bag.__str__()
        self.assertEqual('4:2\n', bag_str)

    def test_count(self):
        bag = Bag.Bag()
        bag.insert(4)
        bag.insert(4)
        bag.insert(4)
        count = bag.count(2)
        self.assertEqual(0, count)

        count = bag.count(4)
        self.assertEqual(3, count)

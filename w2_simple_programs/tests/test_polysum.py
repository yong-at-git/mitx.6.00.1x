from unittest import TestCase
from polysum import polysum


class TestPolysum(TestCase):
    def test_polysum_1(self):
        self.assertEqual(24603725.7333, polysum(77, 62))

    def test_polysum_2(self):
        self.assertEqual(-7.349057708937914e+16, polysum(1, 6))

    def test_polysum_3(self):
        self.assertEqual(39045363.1608, polysum(97, 62))
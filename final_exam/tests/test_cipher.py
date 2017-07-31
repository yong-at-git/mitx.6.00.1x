from unittest import TestCase
import cipher as cr


class TestCipher(TestCase):
    def test_cipher(self):
        map_from = 'abcd'
        map_to = 'dcba'
        code = 'dab'

        expected = ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')
        actual = cr.cipher(map_from, map_to, code)

        self.assertTupleEqual(expected, actual)

from unittest import TestCase
from PrimeNumGenerator import gen_primes


class TestGenPrimes(TestCase):
    def test_gen_primes_2(self):
        expected = 2
        actual = gen_primes().__next__()
        self.assertEqual(expected, actual)

    def test_gen_primes_3(self):

        generator = gen_primes()

        expected = 3
        generator.__next__()
        actual = generator.__next__()
        self.assertEqual(expected, actual)

    def test_gen_primes_5(self):
        # 5 is the 3rd prime number
        generator = gen_primes()

        expected = 5
        for i in range(2):
            generator.__next__()
        actual = generator.__next__()
        self.assertEqual(expected, actual)

    def test_gen_primes_997(self):
        # 997 is the 168th prime number
        generator = gen_primes()

        expected = 997
        for i in range(167):
            generator.__next__()
        actual = generator.__next__()
        self.assertEqual(expected, actual)

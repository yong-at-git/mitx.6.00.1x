from unittest import TestCase
from ..solution.guess_number import GuessNumber

class TestGuessNumber(TestCase):
    def test_guess(self):
        GuessNumber.guess()

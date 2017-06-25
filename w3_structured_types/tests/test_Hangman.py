from unittest import TestCase
import ps3_hangman

class TestHangman(TestCase):
    def test_isWordGuessed_False(self):
        actual = ps3_hangman.isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'])
        self.assertFalse(actual)

    def test_isWordGuessed_True(self):
        actual = ps3_hangman.isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'])
        self.assertTrue(actual)

    def test_getAvailableLetters(self):
        expected = 'abcdfghjlmnoqtuvwxyz'
        actual = ps3_hangman.getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])
        self.assertEqual(expected, actual)

    def test_getGuessedWord_partially(self):
        expected = '_ pp_ e'
        actual = ps3_hangman.getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])
        self.assertEqual(expected, actual)

    def test_getGuessedWord_complete(self):
        expected = 'durian'
        actual = ps3_hangman.getGuessedWord('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u'])
        self.assertEqual(expected, actual)
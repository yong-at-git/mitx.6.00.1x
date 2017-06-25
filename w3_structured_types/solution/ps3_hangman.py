# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "/Users/yong/code/mitx.6.00.1x/w3_structured_types/solution/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False

    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed_so_far = ''
    for letter in secretWord:
        if letter not in lettersGuessed:
            guessed_so_far += '_ '
        else:
            guessed_so_far += letter

    return guessed_so_far


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    from string import ascii_lowercase

    available_letters = ascii_lowercase[:]
    for letter in lettersGuessed:
        available_letters = available_letters.replace(letter, '')

    return available_letters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    secret_word_lowercase = secretWord.lower()

    welcome_greeting = "Welcome to the game, Hangman!"
    print(welcome_greeting)

    length_reminder_format = "I am thinking of a word that is {} letters long."
    print(length_reminder_format.format(len(secret_word_lowercase)))

    split_line = "-------------"

    remaining_guess = 8
    remaining_guess_reminder_format = "You have {} guesses left."

    available_letters_prefix = 'Available letters:'

    good_guess_prefix = "Good guess:"
    repeat_guess_prefix = "Oops! You've already guessed that letter:"
    bad_guess_prefix = "Oops! That letter is not in my word:"
    won = "Congratulations, you won!"
    fail = "Sorry, you ran out of guesses. The word was else."

    input_prompt = 'Please guess a letter:'

    letters_guessed = []

    while remaining_guess > 0:
        print(split_line)

        if isWordGuessed(secret_word_lowercase, letters_guessed):
            print(won)
            return

        print(remaining_guess_reminder_format.format(remaining_guess))
        print(available_letters_prefix, getAvailableLetters(letters_guessed))

        input_letter = input(input_prompt)
        input_letter_lowercase = input_letter.lower()

        if input_letter_lowercase in letters_guessed:
            print(repeat_guess_prefix, getGuessedWord(secret_word_lowercase, letters_guessed))
            continue

        letters_guessed.append(input_letter_lowercase)
        if input_letter_lowercase in secret_word_lowercase:
            print(good_guess_prefix, getGuessedWord(secret_word_lowercase, letters_guessed))
        else:
            print(bad_guess_prefix, getGuessedWord(secret_word_lowercase, letters_guessed))
            remaining_guess -= 1

    print(split_line)
    print(fail)

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
print("The secret word is:", secretWord)
hangman(secretWord)

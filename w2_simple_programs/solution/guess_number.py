class GuessNumber:
    """
        guess a number in the range of [0, 100) in a user's mind
    """

    @staticmethod
    def guess():
        low = 0
        high = 100
        guess = (low + high) // 2

        feedback = ''

        print("Please think of a number between 0 and 100!")
        while feedback != 'c':
            print("Is your secret number %d?" % guess)
            feedback = input(
                "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. "
                "Enter 'c' to indicate I guessed correctly.")
            while len(feedback) != 1 or feedback not in 'hlc':
                print('Sorry, I did not understand your input.')
                print("Is your secret number %d?" % guess)
                feedback = input(
                    "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. "
                    "Enter 'c' to indicate I guessed correctly.")

            if feedback == 'l':
                low = guess
            elif feedback == 'h':
                high = guess
            else:
                print("Game over. Your secret number was: %d" % guess)
                break

            guess = (low + high) // 2


if __name__ == "__main__":
    GuessNumber.guess()

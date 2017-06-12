class GuessNumber:
    """
        guess a number in the range of [0, 100) in a user's mind
    """

    @staticmethod
    def guess():
        lower_bound_inclusive = 0
        upper_bound_exclusive = 100
        guess = (lower_bound_inclusive + upper_bound_exclusive) // 2

        user_feedback = ''

        print("Please think of a number between 0 and 100!")

        while user_feedback != 'c':
            print("Is your secret number %d?" % guess)
            user_feedback = input(
                "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. "
                "Enter 'c' to indicate I guessed correctly.")
            while len(user_feedback) != 1 or user_feedback not in 'hlc':
                print('Sorry, I did not understand your input.')
                print("Is your secret number %d?" % guess)
                user_feedback = input(
                    "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. "
                    "Enter 'c' to indicate I guessed correctly.")

            if user_feedback == 'l':
                lower_bound_inclusive = guess
            elif user_feedback == 'h':
                upper_bound_exclusive = guess
            else:
                print("Game over. Your secret number was: %d" % guess)
                break

            guess = (lower_bound_inclusive + upper_bound_exclusive) // 2


if __name__ == "__main__":
    GuessNumber.guess()

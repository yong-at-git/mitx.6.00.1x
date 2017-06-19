low = 0
high = 100

game_start_msg = 'Please think of a number between 0 and 100!'
input_reminder = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. " \
                 "Enter 'c' to indicate I guessed correctly."
error_input_reminder = 'Sorry, I did not understand your input.'
check_msg = 'Is your secret number'
success_msg = 'Game over. Your secret number was:'

print(game_start_msg)
guess = low + int((high - low) / 2)
print(check_msg, str(guess) + '?')
ans = input(input_reminder)
while ans != 'c':
    if ans == 'h':
        high = guess
    elif ans == 'l':
        low = guess
    else:
        print(error_input_reminder)
        print(check_msg, str(guess) + '?')
        ans = input(input_reminder)
        continue
    guess = low + int((high - low) / 2)
    print(check_msg, str(guess) + '?')
    ans = input(input_reminder)

print(success_msg, guess)

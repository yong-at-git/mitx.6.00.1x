"""
Just run any random piece of code
"""

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 - x) < epsilon:
        print(guess)
        break
    else:
        print(guess)
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
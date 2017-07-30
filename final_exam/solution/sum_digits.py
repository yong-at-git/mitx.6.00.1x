def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    nums = '0123456789'
    digits = []

    for c in s:
        if c in nums:
            digits.append(int(c))

    if len(digits) == 0:
        raise ValueError

    return sum(digits)
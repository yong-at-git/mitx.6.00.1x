def is_in(char, a_str):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    if len(a_str) == 0:
        return len(char) == 0
    if len(a_str) == 1:
        return a_str[0] == char

    low = 0
    high = len(a_str) - 1
    guess = (high - low) // 2

    if a_str[guess] == char:
        return True
    elif a_str[guess] > char:
        return is_in(char, a_str[low:guess])
    else:
        return is_in(char, a_str[(guess + 1):(high + 1)])

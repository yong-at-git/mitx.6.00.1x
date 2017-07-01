def is_triangular(k):
    """
    a triangular is a number which is equals to the sum of continous integers, e.g. 1, 1+2, 1+2+3, 1+2+3+4, etc
    k, a positive integer
    returns True if k is triangular and False if not
    """

    ceiling_half_k = k // 2
    if k % 2 != 0:
        ceiling_half_k = k // 2 + 1

    triangular = 0
    for i in range(1, ceiling_half_k + 1):
        triangular += i
        if triangular == k:
            return True

    return False


def print_without_vowels(s):
    """
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the
    same order they appear in s. Prints this version of s.
    Does not return anything
    """
    vowels = "aeiouAEIOU"
    empty_char = ''
    s_copy = empty_char + s
    for vowel in vowels:
        s_copy = s_copy.replace(vowel, empty_char)
    return s_copy




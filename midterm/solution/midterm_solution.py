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


def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    map_to_occurrences = {}
    for i in L:
        if i in map_to_occurrences:
            map_to_occurrences[i] = map_to_occurrences[i] + 1
        else:
            map_to_occurrences[i] = 1

    keys_odd_occurrences = []

    for j in map_to_occurrences:
        if map_to_occurrences[j] % 2 != 0:
            keys_odd_occurrences.append(j)

    if len(keys_odd_occurrences) == 0:
        return None

    return max(keys_odd_occurrences)


def dict_invert(d):
    """
    d: dict
    Returns an inverted dictionary according to the instructions above
    """
    invert_dict = {}
    for k,v in d.items():
        if v in invert_dict:
            invert_dict[v].append(k)
            invert_dict[v].sort()
        else:
            invert_dict[v] = [k]

    return invert_dict

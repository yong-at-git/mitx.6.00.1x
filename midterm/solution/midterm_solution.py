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
    for k, v in d.items():
        if v in invert_dict:
            invert_dict[v].append(k)
            invert_dict[v].sort()
        else:
            invert_dict[v] = [k]

    return invert_dict


def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    def poly(base):
        num = 0
        power_idx = len(L)
        for n in L:
            num += n * (base ** (power_idx - 1))
            power_idx -= 1
        return num

    return poly


def is_list_permutation(L1, L2):
    """
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    """
    def map_to_occurrence(l):
        dict_occurrence = {}
        for elem in l:
            if elem in dict_occurrence:
                dict_occurrence[elem] = dict_occurrence[elem] + 1
            else:
                dict_occurrence[elem] = 1
        return dict_occurrence

    if len(L1) == 0 and len(L2) == 0:
        return None, None, None

    if len(L1) != len(L2):
        return False

    dict_occurrence_l1 = map_to_occurrence(L1)
    dict_occurrence_l2 = map_to_occurrence(L2)

    if dict_occurrence_l2 != dict_occurrence_l1:
        return False

    max_occurrence = max(dict_occurrence_l1.values())

    for k, v in dict_occurrence_l1.items():
        if v == max_occurrence:
            return k, v, type(k)

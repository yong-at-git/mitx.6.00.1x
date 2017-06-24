def naive_fib(n):
    """
    Calculates Fibonacci number naively by simply using recursion
    :param n:
    :return:
    """
    if n in [1, 2]:
        return 1

    return naive_fib(n - 1) + naive_fib(n - 2)


def fib_with_dict(n, a_dict):
    """
    Calculates Fibonacci number, in an efficient way by using dictionary to memorize already calculated values.
    :param n:
    :param a_dict: with a_dict[1] and a_dict[2] initialized
    :return:
    """
    if n in a_dict:
        return a_dict[n]

    n_value = fib_with_dict(n - 1, a_dict) + fib_with_dict(n - 2, a_dict)
    a_dict[n] = n_value

    return n_value

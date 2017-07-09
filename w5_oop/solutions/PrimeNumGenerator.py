def gen_primes():
    """
    Generates the sequence of prime numbers. Calls to next() of the sequence will return prime numbers successively.
    :return: a sequence of prime numbers
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    num = 2
    while True:
        if is_prime(num):
            yield num

        num += 1

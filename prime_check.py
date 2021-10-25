import random


def FastMod(a, i, n):
    """ Fast modular division
    :param a:
    :param i:
    :param n:
    :return: a**i mod n
    """

    x = 1
    for _ in range(i):
        x = (x*a) % n

    return x


def FermatTest(n, k):
    """ Check is n pseudoprime by Fermat test.
    :param n: number
    :param k: how many different tests needs to check.
    :return: is n pseudoprime.
    """

    a_tests = []
    i = 2
    while len(a_tests) < k:
        if n % i != 0:
            a_tests.append(i)
        i += 1

    for a in a_tests:
        if FastMod(a, n-1, n) != 1:
            return False

    return True


def MillerRabinTest(n, k):
    """ Check is n prime by Miller-Rabin test.
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    :param n: number
    :param k: how many different tests needs to check.
    :return: is n prime
    """

    if n % 2 == 0:
        return False

    # n - 1 = 2 ** r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # do k tests of prime number
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = FastMod(a, d, n)

        if x == 1 or x == n - 1:
            continue

        condition2 = False
        for i in range(r-1):
            x = x**2 % n
            if x == n - 1:
                condition2 = True
                break
        if condition2:
            continue
        else:
            return False

    return True


def task1(n, k):
    """ Search pseudoprimes numbers in [4, n] by Ferma test.
    :param n: max number
    :param k: how many tests needs to check.
    :return: list of pseudoprimes
    """

    return [i for i in range(4, n) if FermatTest(i, k)]


def task2(n, k):
    """ Search primes numbers in [4, n] by Miller-Rabin algo.
        :param n: max number
        :param k: how many tests needs to check.
        :return: list of primes
        """

    return [i for i in range(4, n) if MillerRabinTest(i, k)]


n = 1000
tests = 2

pseudoprimes = task1(n, tests)
primes = task2(n, tests)

print(f'Pseudprimes: {" ".join([str(el) for el in pseudoprimes])}')
print(f'Primes: {" ".join([str(el) for el in primes])}')

notprimes = sorted(list(set(pseudoprimes) - set(primes)))
print(f'Not prime pseudoprimes: {" ".join([str(el) for el in notprimes])}')

# print(FermaTest(41041, 20))

"""Binomial coefficient calculations for choosing k items from n."""


def factorial(n):
    """Return the factorial of a non-negative integer.

    Args:
        n: Integer whose factorial is to be computed.

    Returns:
        The product of all integers from 1 through ``n``.
    """
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


def main(n, k):
    """Calculate the binomial coefficient for choosing ``k`` items from ``n``.

    The result is equivalent to the "n choose k" formula. For example, in a
    5-card poker game with a standard deck, ``n = 52`` and ``k = 5``.

    Args:
        n: Total number of items available.
        k: Number of items to choose.

    Returns:
        The value of ``n choose k``.
    """
    a = factorial(n)
    b = factorial(k)
    c = factorial(n-k)

    return a / (b*c)


if __name__=='__main__':
    print('*** Welcome to Binomial Coefficient! ***')
    print()
    print('The binomial coefficient can also be called the "n choose k" formula')
    print('n is the total number of available things')
    print('k is the number of items to choose out of n')
    print('example: in a 5-card poker game with a standard deck, k = 5, n = 52')
    n = int(input('Enter an (n) value: '))
    k = int(input('Enter a (k) value: '))
    num = main(n, k)
    print(f'{num:,}')


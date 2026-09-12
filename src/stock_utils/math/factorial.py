"""Recursive factorial implementation."""


def factorial(n):
    """Return the factorial of a positive integer recursively.

    Args:
        n: Integer whose factorial is to be computed.

    Returns:
        The product of all integers from 1 through ``n``.
    """
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    x = int(input('Enter a starting point: '))
    num = factorial(x)
    print(f'{num:,}')

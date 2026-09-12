"""Sieve of Eratosthenes prime generation utilities."""


def prime_finder(upper_bound):
    """Return all prime numbers up to ``upper_bound``.

    Args:
        upper_bound: Maximum value to consider.

    Returns:
        A set containing each prime number less than or equal to
        ``upper_bound``.
    """
    primes = set()
    composites = set()
    n = 2
    while n < upper_bound+1:
        if n not in composites:
            primes.add(n)
        first_composite = n ** 2
        composites.add(first_composite)
        for x in range(n+1, upper_bound + 1):
            c = x * n
            if c <= upper_bound:
                composites.add(c)
        n += 1
    
    return primes


def sieve_of_eratosthenes(upper_bound):
    """Build a visual list of numbers and their prime/non-prime status.

    Args:
        upper_bound: Largest value to include in the generated matrix.

    Returns:
        A dictionary containing both the full range and a filtered view showing
        only prime values.
    """
    full_list = list()
    filtered_list = list()
    if upper_bound % 10 == 0:
        num_rows = int(upper_bound / 10) + 1
    else:
        num_rows = int(upper_bound / 10) + 2

    for j in range(1, num_rows):
        m = list()
        for a in range(1, 11):
            val = (j-1) *10 + a
            m.append(val)

        primes = prime_finder(upper_bound)
        k = list()
        for x in range(1,11):
            val = (j-1) * 10 + x
            if val not in primes:
                val = '.'
            k.append(val)

        filtered_list.append(k)
        full_list.append(m)

    output = {
            'full_list': full_list,
            'filtered_list': filtered_list,
            }
    return output


if __name__ == '__main__':
    limit = int(input('Enter an upper boundary: '))
    print('Sieve of Eratosthenes')
    print()
    print('https://share.google/images/HMAxLTOtUsFByKiyv')
    
    matrix = sieve_of_eratosthenes(limit)
    print('All numbers in given range:')

    for i in range(len(matrix['full_list'])):
        print(matrix['full_list'][i])

    print()
    print('Only the primes within the given range')
    print()
    for j in range(len(matrix['filtered_list'])):
        print(matrix['filtered_list'][j])






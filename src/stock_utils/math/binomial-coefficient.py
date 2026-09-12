def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


def main(n, k):
    # The binomial coefficient can also be called the "n choose k" formula
    # n is the total number of available things
    # k is the number of items to choose out of n
    # example: in a 5-card poker game with a standard deck, k = 5, n = 52
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


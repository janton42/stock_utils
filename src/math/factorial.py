def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    x = int(input('Enter a starting point: '))
    num = factorial(x)
    print(f'{num:,}')

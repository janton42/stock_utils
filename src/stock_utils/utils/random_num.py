"""Random integer and float generation helpers."""

import random


def display_rand_int(minimum, maximum):
    """Generate and print a random integer within a range.

    Args:
        minimum: Lower bound for the random integer.
        maximum: Upper bound for the random integer.

    Returns:
        The generated random integer.
    """
    random_int = random.randint(minimum, maximum)
    print(f'The number is: {random_int}')
    return random_int


def gen_random_float(mi, ma):
    """Generate and print a random float within a range.

    Args:
        mi: Lower bound for the random float.
        ma: Upper bound for the random float.

    Returns:
        The generated random float.
    """
    random_float = random.uniform(mi, ma)
    print(f'The number is: {random_float}')
    return random_float


if __name__ == '__main__':
    options = ['Random Integer', 'Random Float']
    for i,ch in enumerate(options):
        print(f'{i+1}: {ch}')
    choice = int(input('Enter your choice: '))
    mi = input("Enter a min: ")
    ma = input("Enter a max: ")
    if choice == 1:
         mi = int(mi)
         ma = int(ma)
         display_rand_int(mi, ma)
    elif choice == 2:
         mi = float(mi)
         ma = float(ma)
         gen_random_float(mi, ma)
    else:
        print('Womp Womp. Invalid entry, try again')




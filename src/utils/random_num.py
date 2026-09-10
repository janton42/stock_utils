import random

def display_rand_int(minimum, maximum):
    random_int = random.randint(minimum, maximum)
    print(f'The number is: {random_int}')
    return random_int

def gen_random_float(mi, ma):
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




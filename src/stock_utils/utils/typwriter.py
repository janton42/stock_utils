import time
import random

def typwriter_print(text: str):
    for char in text:
        delay = random.uniform(0.09, 0.13)
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


if __name__ == '__main__':
    typwriter_print('Welcome to Typwriter Print Demo!')
    time.sleep(2)
    typwriter_print('Enter some text below to try it yourself!')
    text = input('Input: ')
    typwriter_print(text)

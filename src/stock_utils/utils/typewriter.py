"""Typewriter-style terminal output helper."""

import time
import random


def typewriter_print(text: str):
    """Print text as if it were being typed one character at a time.

    Args:
        text: Message to display with a brief random delay between characters.
    """
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

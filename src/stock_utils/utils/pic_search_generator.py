"""Random phrase generator for image search prompts."""

import random

main_subjects = ['cat', 'dog', 'police car', 'tree', 'banana', 'cell phone', 'smart phone']

backgrounds = ['outer space', 'a green field', 'a cold steel cage', 'a beach']


def gen_rand_int(x: list):
    """Return a random valid index for a list.

    Args:
        x: Sequence to index into.

    Returns:
        A random integer between 0 and ``len(x) - 1``.
    """
    maximum = len(x) - 1
    random_int = random.randint(0, maximum)
    return random_int


def gen_phrase():
    """Generate a random image-search phrase using a subject and background.

    Returns:
        A descriptive phrase like "cat in a green field".
    """
    return f'{main_subjects[gen_rand_int(main_subjects)]} in {backgrounds[gen_rand_int(backgrounds)]}'


if __name__ == '__main__':
    print(gen_phrase())

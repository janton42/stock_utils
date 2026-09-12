"""Palindrome checking utilities."""


def is_palindrome(s: str) -> bool:
    """Return whether a string reads the same forwards and backwards.

    Args:
        s: String to evaluate.

    Returns:
        True if the string is a palindrome; otherwise False.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


if __name__ == '__main__':
    word = input('Enter a word: ')
    print(is_palindrome(word))

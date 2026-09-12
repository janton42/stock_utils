
"""Binary search implementation for sorted collections."""


def binary_search(target, space):
    """Return whether a target value exists in a sorted sequence.

    Args:
        target: Value to look for in the sequence.
        space: Sorted sequence of comparable values.

    Returns:
        True if the target is present; otherwise False.
    """
    left = 0
    right = len(space) - 1

    while left <= right:
        mid = (left + right) // 2
        if space[mid] == target:
            return True
        elif space[mid] < target:
            left = mid + 1
        elif space[mid] > target:
            right = mid - 1
    return False

if __name__ == '__main__':
    space = list(input('Enter the SORTED list:'))
    target = int(input('Enter a search target:'))
    print(binary_search(target, space))


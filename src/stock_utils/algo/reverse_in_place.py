"""In-place list reversal utility."""


def reverse_in_place(arr):
    """Reverse a list in place.

    Args:
        arr: List to reverse.

    Returns:
        The reversed list.
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

    return arr


if __name__ == '__main__':
    arr = input('Input values for the array as one input without spaces:')
    arr_reversed = reverse_in_place(list(arr))
    print(arr_reversed)

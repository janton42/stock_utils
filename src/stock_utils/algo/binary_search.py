
def binary_search(target, space):
    left = 0
    right = len(space) - 1

    while left <= right:
        mid = (left + right) // 2
        if space[mid] == target:
            return True
        elif space[mid] < target:
            left = mid + 1
        elif space[mid] > target:
            right = mid -1 
    return False

if __name__ == '__main__':
    space = list(input('Enter the SORTED list:'))
    target = int(input('Enter a search target:'))
    print(binary_search(target, space))


def rotate_array(nums: list[int], k: int) -> list[int]:
    if not nums or k == 0:
        return nums[:]

    # normalize k
    n = len(nums)
    k %= n
    # set the index, at which to split
    split = n - k
    # rotating by slicing
    ## combine the last k elements + the first k elements
    return nums[split:] + nums[:split]



if __name__=='__main__':
    nums = list(input('Enter items for the list as a string:'))
    k = int(input('Enter a number of times to rotate (integer):'))
    print(rotate_array(nums, k))



def compare_strings(s1: str, s2: str) -> int:
    # return -1 if s1 < s2, 0 if s1 == s2, 1 if s1 > s2
    if s1 == s2:
        return 0
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] < s2[j]:
            return -1
        elif s1[i] > s2[i]:
            return 1
        i += 1
        j += 1

    if len(s1) < len(s2):
        return -1
    else:
        return 1



if __name__ == '__main__':
    s1 = input('Enter the first string to compare:')
    s2 = input('Enter the second string to compare:')

    print(compare_strings(s1,s2))

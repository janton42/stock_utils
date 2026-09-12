def find_longest_palindrome(s):
    longest = ''
    len_long = 0
    for i in range(len(s)):
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > len_long:
                longest = s[left:right + 1]
                len_long = right - left + 1
            left -= 1
            right += 1

        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > len_long:
                longest = s[left:right + 1]
                len_long = right - left + 1
            left -= 1
            right += 1

    return longest

if __name__ == '__main__':
    word = input('Enter a word:')
    print(find_longest_palindrome(word))

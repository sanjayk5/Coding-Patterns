def is_palindrome(s):
    left = 0
    right = len(s) - 1
    # use two pointers to traverse the string
    while left <= right:
        if s[left] == s[right]:
            left = left + 1
            right = right - 1
            continue
        else:
            return False

    return True


# src_str = "madam"
src_str = "ABCBa"
print("The given string is palindrome: ", is_palindrome(src_str))

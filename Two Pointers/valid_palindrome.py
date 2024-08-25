def is_palindrome(s):
    left = 0
    right = len(s) - 1
    # use two pointers to traverse the string
    while left <= right:
        if s[left] != s[right]:
            return False

        left = left + 1
        right = right - 1
    return True


def main():
    test_strings = ["madam", "ABCB", "abcdcba", "abba", "MaDam"]
    for test in test_strings:
        print(f"The given string {test} is palindrome: ", is_palindrome(test))


if __name__ == "__main__":
    main()

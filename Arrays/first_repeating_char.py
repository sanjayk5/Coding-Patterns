def findFirstRepeatingCharacter(str: str) -> str:
    charMap = {}
    for ch in str:
        if charMap.get(ch):
            return ch
        charMap[ch] = True
    return None

# time complexity = O(n), space complexity O(n)

print(findFirstRepeatingCharacter("abcde"))
print(findFirstRepeatingCharacter("responsibility"))
print(findFirstRepeatingCharacter("abcabc"))
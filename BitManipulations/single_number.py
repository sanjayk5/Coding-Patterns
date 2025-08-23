def single_number(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR cancels duplicates
    return result

# Example
print(single_number([4, 1, 2, 1, 2]))  # 4
print(single_number([1, 2, 1, 2, 5]))  # 5

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Example
print(is_power_of_two(16))  # True (10000)
print(is_power_of_two(18))  # False

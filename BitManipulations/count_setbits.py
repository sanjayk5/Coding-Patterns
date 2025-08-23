# Hamming weight of a number
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1

    return count


if __name__ == "__main__":
    print(count_set_bits(10))  # 10 = 1010 in binary → 2
    print(count_set_bits(29))  # 29 = 11101 in binary → 4

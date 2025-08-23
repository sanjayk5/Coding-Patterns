def swap_even_odd_bits(n):
    # Masks for 32-bit
    EVEN_MASK = 0xAAAAAAAA  # 101010...10 (even bit positions)
    ODD_MASK  = 0x55555555  # 010101...01 (odd bit positions)
    
    # Extract even and odd bits
    even_bits = n & EVEN_MASK
    odd_bits  = n & ODD_MASK
    
    # Shift even bits right, odd bits left
    even_bits >>= 1
    odd_bits  <<= 1
    
    # Combine
    return (even_bits | odd_bits) & 0xFFFFFFFF  # ensure 32-bit result


# 🔹 Example
num = 23   # Binary: 0001 0111
swapped = swap_even_odd_bits(num)
print(f"Original: {num} -> {bin(num)}")
print(f"Swapped : {swapped} -> {bin(swapped)}")

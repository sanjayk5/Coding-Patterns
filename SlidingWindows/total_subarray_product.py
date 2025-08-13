from typing import List

def num_subarrays_product_less_than_k(nums: List[int], k: int) -> int:
    """
    Variable window (all nums > 0).
    Return the count of contiguous subarrays with product < k.
    Time: O(n), Space: O(1)
    """
    if k <= 1:
        return 0
    prod = 1.0
    left = 0
    count = 0
    for right, x in enumerate(nums):
        prod *= x
        while prod >= k and left <= right:
            prod /= nums[left]
            left += 1
        count += right - left + 1

    return count



if __name__ == "__main__":
    # Number of subarrays with product < k (positives)
    nums, k= [10, 5, 2, 6], 100
    out = num_subarrays_product_less_than_k(nums, k)
    print("num_subarrays_product_less_than_k:", out)  # Expected: 8
    assert out == 8


from typing import List
def longest_subarray_sum_leq_k_nonneg(nums: List[int], k: int) -> int:
    """
    Variable window (all nums assumed non-negative).
    Return the maximum length of a subarray with sum <= k.
    Time: O(n), Space: O(1)
    """
    left = 0
    total = 0
    best = 0
    for right, x in enumerate(nums):
        total += x
        while total > k and left <= right:
            total -= nums[left]
            left += 1
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    # Longest subarray with sum <= k (non-negative)
    nums, k4 = [1, 2, 1, 0, 1, 1, 0], 4
    out = longest_subarray_sum_leq_k_nonneg(nums, k4)
    print("longest_subarray_sum_leq_k_nonneg:", out)  # Expected: 5
    assert out == 5


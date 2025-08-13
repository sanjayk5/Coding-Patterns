
from collections import defaultdict
from typing import List

def longest_subarray_at_most_k_distinct(nums: List[int], k: int) -> int:
    """
    Variable window with frequency map.
    Return the length of the longest subarray containing at most k distinct values.
    Time: O(n), Space: O(k)
    """
    left = 0
    freq = defaultdict(int)
    distinct = 0
    best = 0
    for right, x in enumerate(nums):
        if freq[x] == 0:
            distinct += 1
        freq[x] += 1
        while distinct > k:
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                distinct -= 1
            left += 1
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    # Longest subarray with at most k distinct elements
    nums, k = [1, 2, 1, 2, 3], 2
    out = longest_subarray_at_most_k_distinct(nums, k)
    print("longest_subarray_at_most_k_distinct:", out)  # Expected: 4
    assert out == 4


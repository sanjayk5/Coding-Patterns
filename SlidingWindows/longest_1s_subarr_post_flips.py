from typing import List


def longest_ones_after_flips(nums: List[int], k: int) -> int:
    """
    Binary array; variable window.
    Return the longest subarray containing only 1s after flipping at most k zeros.
    Time: O(n), Space: O(1)
    """
    left = 0
    zeros = 0
    best = 0
    for right, x in enumerate(nums):
        if x == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    nums, k = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
    out = longest_ones_after_flips(nums, k)
    print("longest_ones_after_flips:", out)  # Expected: 10
    assert out == 10
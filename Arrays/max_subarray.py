# Maximumsubarray sum (Kadane's algo)
# Time: O(n), Space: O(1)
def max_subarray(nums: list[int]) -> int:
    max_sum = cur_sum = nums[0]
    for n in nums[1:]:
        cur_sum = max(n, cur_sum + n)
        max_sum = max(max_sum, cur_sum)
    return max_sum

# Example
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # 6 (subarray: [4,-1,2,1])

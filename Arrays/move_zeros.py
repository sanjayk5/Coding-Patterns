from typing import List
class Solution:
    def move_zeros_inplace(self, nums: List[int]):
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1
        for x in range(j, len(nums)):
            nums[x] = 0

        print(nums)


array = [0, 15, 3, 9, 0, 5, 0, 10]
s = Solution()
s.move_zeros_inplace([0, 15, 3, 9, 0, 5, 0, 10])

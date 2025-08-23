# Product of array without current element
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [1] * n
    
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    
    return res

# Example
print(product_except_self([1,2,3,4]))  # [24,12,8,6]

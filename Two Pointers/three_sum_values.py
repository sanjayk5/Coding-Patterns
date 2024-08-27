def find_threesum_values(nums, target):
    nums.sort() # time complexity= O(nlog n), space complexity O(n)

    # time complexity for nested loop= O(n^2)
    # condition: nums[i]+nums[j]+nums[k]= target and i != j, j != k, k != i
    for i in range(0, len(nums) - 2):
        low = i + 1
        high = len(nums) - 1

        while low < high:
            sum = nums[i] + nums[low] + nums[high]

            if sum == target:
                return True
            elif sum < target:
                low += 1
            else:
                high -= 1

    return False


def main():
    num_list = [4, 6, 2, -5, 10, 9]
    target_sum = 25

    if find_threesum_values(num_list, target_sum):
        print(f"Sum for {target_sum} exists in the list {num_list}")
    else:
        print(f"Sum for {target_sum} done not exist in the list {num_list}")


if __name__ == '__main__':
    main()

def binary_search(arrnums, num):
    low = 0
    high = len(arrnums) - 1

    while low <= high:
        mid = (low+high) // 2

        if arrnums[mid] == num:
            return mid
        elif arrnums[mid] < num:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [1, 2, 3, 4, 5, 6] # sorted array for binary search to work
target = 5

result = binary_search(arr, target)

if result != -1:
    print("Element is present at index %d" %result)
else:
    print("Element is not present")
def max_sum(arr, window_size):
    arr_size = len(arr)
    if arr_size <= window_size:
        print("Invalid window size specified")
        return -1

    cur_window_sum = sum(arr[i] for i in range(window_size))
    max_sum = cur_window_sum

    for i in range(arr_size - window_size):
        cur_window_sum = cur_window_sum - arr[i] + arr[i+window_size]
        max_sum = max(cur_window_sum, max_sum)

    return max_sum


array = [10, -30, 50, 70, 20, 90, -25, 35, 60]
k = 2
answer = max_sum(array, k)
print("Maximum sum with window size of " + str(k) + " is " + str(answer))
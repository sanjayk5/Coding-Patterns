# Time complexity= O(nlogn), space complexity O(1)
def findPair(arr, k):
    arr.sort() # sort the array in place O(nlogn)
    i = 0
    j = len(arr) - 1
    
    while i < j:
        if arr[i] + arr[j] == k:
            return True
        elif arr[i] + arr[j] > k:
            j -= 1
        else:
            i += 1
    return False


# Time complexity= O(n), space complexity O(n)
def pairSums(arr, k):
    visited = {}
    for ele in arr:
        if visited.get(k - ele): # O(1) lookup
            return True
        visited[ele] = True # O(1) insertion
    return False


arr = [4, 5, 1, -3, 6]
k = 11
print(findPair(arr, k))

arr2 = [4, 5, 1, -3, 6]
k = 8
print(pairSums(arr2, k))
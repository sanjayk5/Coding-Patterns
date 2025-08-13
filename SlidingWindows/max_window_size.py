from typing import List
from collections import deque

def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """
    Fixed-size window with deque.
    Return the max for each window of size k.
    Time: O(n), Space: O(k)
    """
    if k <= 0:
        return []
    dq = deque()  # indices with decreasing values
    res = []
    for i, x in enumerate(nums):
        # drop indices out of window
        if dq and dq[0] <= i - k:
            dq.popleft()
        # maintain decreasing deque
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res

if __name__ == "__main__":
    nums, k = [1, 3, -1, -3, 5, 3, 6, 7], 3
    out = max_sliding_window(nums, k)
    print("max_sliding_window:", out)  # Expected: [3, 3, 5, 5, 6, 7]
    assert out == [3, 3, 5, 5, 6, 7]


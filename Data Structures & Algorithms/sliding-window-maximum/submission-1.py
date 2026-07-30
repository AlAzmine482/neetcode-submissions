from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        n = len(nums)
        output = []
        for i, num in enumerate(nums):
            # 1. Pop smaller elements from back
            # While deque is NOT empty AND the value at the back is <= current num
            while q and nums[q[-1]] <= num:
                q.pop()
            # 2. Add current index to back
            q.append(i)
            # 3. Pop out-of-bounds index from front
            if q[0] < i - k + 1:
                q.popleft()
            # 4. Append max to output if window is full size (i >= k - 1)
            if i >= k - 1:
                output.append(nums[q[0]])
        return output
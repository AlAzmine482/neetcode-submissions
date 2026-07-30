class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return 0
        n = len(nums)
        
        output = []
        for i in range(n - k + 1):
            curr_sum = 0
            window_max=nums[i]
            for j in range(k):
                window_max = max(window_max, nums[i + j])
            output.append(window_max)
        return output
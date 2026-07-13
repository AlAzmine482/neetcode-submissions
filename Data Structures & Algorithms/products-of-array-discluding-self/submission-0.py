class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res  = [1] * n
        for i in range(n):
            for j in range(n):
                if i != j:
                    res[i] *= nums[j]
        return res
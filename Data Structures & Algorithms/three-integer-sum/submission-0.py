class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #nums=[-1,0,1,2,-1,-4]
        nums.sort() #O(n*log(n)) time
       # print(nums)#[-4, -1, -1, 0, 1, 2]
        res = []
        for i in range(len(nums)-1):
           # print(i)#0,1,2,3,4
            sumVal = - nums[i]
            #print(sumVal)
            left = i + 1
            #print(left)
            right = len(nums) - 1
            #print(right)
            while (left != right):
                if(nums[left]+nums[right] == sumVal):
                    if [nums[i],nums[left],nums[right]] not in res: res.append([nums[i],nums[left],nums[right]])
                    right -= 1 # we can either move right or left, doesn't matter, since if its the same value again
                    # we would have a duplicate entry anyways. With duplciated we'd need to consider the left, right 
                    # edge case which is harder
                    continue
                if(nums[left]+nums[right] > sumVal):
                    right -= 1
                else:
                    left += 1
        return res
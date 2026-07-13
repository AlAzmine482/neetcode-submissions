#Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

#A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

#You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number = set(nums)
        count = 0;
        for each in number: 
            streak, curr = 0, each
            while curr in number:
                  streak += 1
                  curr += 1
                  count = max(count, streak)
        return count
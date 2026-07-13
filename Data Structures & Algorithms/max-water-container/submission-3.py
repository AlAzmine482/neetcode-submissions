class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            width = right - left
            current_height = min(heights[left], heights[right])
            #print(heights[left]) #1 ,7,7,7,7,7,7
            #print(heights[right]) #6,6,3,7,4,5,2
            #print(current_height) # 1,6,3,7,4,5,2
            #print(width)#7,6,5,4,5,3,2,1,
            current_area = width * current_height
            #print(current_area) #7,36,15,28,12,10
            # Update max_area if we found a bigger container
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
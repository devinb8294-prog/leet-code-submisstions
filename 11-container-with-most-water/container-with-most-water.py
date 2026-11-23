class Solution:
    def maxArea(self, height: list[int]) -> int:
        #Two pointer approach
        #Left and right side
        #Each iteration calulate the area. (shorter height x (index-index))
        #Save max area, move shorter height on each iteration

        left = 0
        right = len(height) - 1

        area = 0

        while left < right:
            new_area = min(height[left], height[right]) * (right - left)

            if new_area > area:
                area = new_area
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return area
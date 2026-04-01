class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        area = 0
        while left < right:
            left_height = heights[left]
            right_height = heights[right]
            height = min(left_height,right_height)
            width = right - left
            current_area = height*width
            area = max(area,current_area)
            if left_height < right_height:
                left+=1
            elif left_height > right_height:
                right-=1
            else:
                left+=1
                right-=1
        return area
            


            
            

        
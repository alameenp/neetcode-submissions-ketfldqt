class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0
        while left < right:
            left_h = heights[left]
            right_h = heights[right]
            curr_area = min(left_h,right_h)*(right-left)
            area = max(curr_area,area)
            if left_h < right_h:
                left += 1
            else:
                right -= 1
        return area
        
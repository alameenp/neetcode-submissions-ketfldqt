class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2
            mid_value = nums[mid]
            if l==r:
                return mid_value

            if mid_value < nums[r]:
                r = mid
                continue

            if mid_value > nums[r]:
                l = mid+1
                continue
            

            
            


        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()
        
        for curr,target in enumerate(nums):
            if curr > 0 and nums[curr-1] == target:
                continue
            l = curr+1
            r = n-1
            while l < r:
                left = nums[l]
                right = nums[r]
                if r < n-1 and nums[r+1]==right:
                    r-=1
                    continue
                if l > curr + 1 and nums[l-1] == left:
                     l+=1
                     continue
                summ = target+left+right
                if summ > 0:
                    r-=1
                    continue
                elif summ < 0:
                    l+=1
                    continue
                else:
                    result.append([target,left,right])
                    r-=1
                    l+=1
        return result

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = 0
        for i in nums:
            if curr_sum+i>= i:
                curr_sum += i
                max_sum = max(curr_sum,max_sum)
                continue
            else:
                curr_sum = i
                max_sum = max(curr_sum,max_sum)
                continue
        return max_sum

            
            


            




            
        
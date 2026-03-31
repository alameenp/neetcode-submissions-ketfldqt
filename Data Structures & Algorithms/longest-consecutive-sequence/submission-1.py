from collections import deque
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique_nums = set(nums)
        length = 1
        for num in unique_nums:
            temp_length = 1
            if num-1 in unique_nums:
                consecutive = num-1
                stop = True
                while stop:
                    if consecutive in unique_nums:
                        temp_length += 1
                        consecutive -= 1
                    else:
                        length = max(temp_length, length)
                        stop = False
        
        return length
                    
                
                


                


        
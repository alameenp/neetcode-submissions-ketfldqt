class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique_nums = set(nums)
        length = 0
        for num in unique_nums:
            current_length = 0
            if num-1 not in unique_nums:
                current_length +=1
                start = num
                while start+1 in unique_nums:
                    current_length+=1
                    start+=1
                length = max(length, current_length)
        return length
                
            




                


        
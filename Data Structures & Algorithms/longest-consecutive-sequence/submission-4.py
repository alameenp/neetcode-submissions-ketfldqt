class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        sequence_length = 0
        current_sequence_length = 0
        for num in nums_set:
            if not(num-1 in nums_set):
                current_sequence_length = 1
                start = num
                while start+1 in nums_set:
                    current_sequence_length+=1
                    start+=1
                
            sequence_length = max(current_sequence_length,sequence_length)
        return sequence_length

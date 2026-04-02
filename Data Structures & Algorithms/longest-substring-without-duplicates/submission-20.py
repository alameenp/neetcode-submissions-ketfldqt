class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        unique_dict = {}
        max_length = 0
        if not s:
            return 0
        for right, elem in enumerate(s):
            if elem in unique_dict and unique_dict[elem] >= left :
                left = unique_dict[elem]+1
            unique_dict[elem] = right
            max_length = max(max_length, right - left+1)
        return max_length

                
            
                
        

        
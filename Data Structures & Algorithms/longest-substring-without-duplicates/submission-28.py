class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_dict = {} 
        left = 0
        for right, char in enumerate(s):
            if char in char_dict and char_dict[char]>=left:
                left = char_dict[char]+1
            char_dict[char] = right
            max_length = max(max_length,right-left+1)


        return max_length
            


            
            
                

            

            

        
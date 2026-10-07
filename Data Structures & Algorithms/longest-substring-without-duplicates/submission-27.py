class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_dict = {} 
        i = 0
        left = 0
        while i < len(s):
            if char_dict.get(s[i]) is None:
                char_dict[s[i]] = i
                curr_length = i-left+1
                max_length = max(max_length, curr_length)
                i+=1
            elif char_dict[s[i]] >= left:
                left = char_dict[s[i]] + 1
                char_dict[s[i]] = i
                i += 1
            else:
                curr_length = i-left+1
                max_length = max(max_length, curr_length)
                char_dict[s[i]] = i
                i+=1

        return max_length
            


            
            
                

            

            

        
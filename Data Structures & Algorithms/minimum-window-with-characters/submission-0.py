class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_count = {}
        t_count = {}
        result_left = 0
        result_length = float('inf')
        for i in range(len(t)):
            t_count[t[i]] = t_count.get(t[i],0)+1
        
        need = len(t_count)
        if not need:
            return ""
        have = 0
        left = 0
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char,0)+1
            if char in t_count and t_count[char] == window_count[char]:
                have += 1
            if have >= need:
                while have == need:
                    current_length = right - left + 1
                    if current_length < result_length:
                        result_left = left
                        result_length = int(right - left+1)
                    left_char = s[left]
                    if left_char in t_count and window_count[left_char] == t_count[left_char]:
                        have -= 1
                    window_count[s[left]] -= 1
                    left += 1
        if result_length == float('inf'):
            return ""
        
        return s[result_left:result_left+result_length]
                    


            
            




            
            
            



            

        

            

        
            
        
        
        
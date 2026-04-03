class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        result = 0
        max_frequency = 0
        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right],0)+1
            max_frequency = max(max_frequency, counts[s[right]])
            if right - left + 1 - max_frequency > k:
                counts[s[left]]-=1
                left+=1
            result = max(result, right-left+1)
        return result
                

            

            
            

                
            
                
        
            
        

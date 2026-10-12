from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        need = Counter(t)
        met = 0
        have = Counter()
        l = 0
        best_l,best_len = 0,float('inf')

        for r,c in enumerate(s):
            if c in need:
                have[c] +=1
                if have[c] == need[c]:
                    met+=1
            
            if met < len(need):
                continue

            while s[l] not in need or need[s[l]] < have[s[l]]:
                if s[l] in need:
                    have[s[l]] -= 1
                l+=1

            if r-l+1 < best_len:
                best_l,best_len = l, r-l+1
        
        return "" if best_len == float('inf') else s[best_l:best_l+best_len]

                
                        


            



        

                
                
                

        
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        need = dict()
        for i in t:
            need[i] = need.get(i,0)+1
        requirements_met = 0
        have = {}
        r = l = 0
        min_length = len(s)

        l_min = 0
        r_min = len(s) -1
        while r < len(s):
            if s[r] in need:
                have[s[r]] = have.get(s[r],0)+1
                if have[s[r]] == need[s[r]]:
                    requirements_met+=1
            
            if requirements_met == len(need):
                while r-l+1 >= len(t):
                    if min_length > r - l+1:
                        l_min = l
                        r_min = r
                        min_length = r-l+1
                    
                    if s[l] in need and need[s[l]]==have[s[l]]:
                        break

                    if s[l] in need and need[s[l]] < have[s[l]]:
                        have[s[l]] -= 1

                    l+=1
                    
            r+=1
        
        if requirements_met == len(need):
            return s[l_min:r_min+1]
        else:
            return ""
                    
                        


            



        

                
                
                

        
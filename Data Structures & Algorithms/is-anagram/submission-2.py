class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = dict()
        for i in s:
            if dict_s.get(i) is None:
                dict_s[i] = 1
                continue
            dict_s[i]+=1
        
        for j in t:
            if dict_s.get(j) is None:
                return False
            dict_s[j]-=1
            if dict_s[j]== 0:
                del dict_s[j]
        if len(dict_s)!=0:
            return False
        return True
        
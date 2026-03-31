class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)<=1:
            return False
        for i in range(len(s)):
            if s[i] in ('[','(','{'):
                stack.append(s[i])
            if s[i] in (']',')','}'):
                if len(stack)==0:
                    return False
                last_open = stack.pop(-1)
                if s[i] == ']' and last_open != '[':
                    return False
                if s[i] == ')' and last_open != '(':
                    return False
                if s[i] == '}' and last_open != '{':
                    return False
        if len(stack)!= 0:
            return False
        return True

                


            
            


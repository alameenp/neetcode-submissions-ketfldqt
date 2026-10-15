from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        if len(s)==1:
            return False
        for c in s:
            if c in ["(","{","["]:
                stack.append(c)
            else:
                if not stack:
                    return False 
                if c == "]" and stack.pop() == "[" :
                    continue
                
                if c == "}" and stack.pop() == "{" :
                    continue
                
                if c == ")" and stack.pop() == "(" :
                    continue
                else:
                    return False
        
        return True if not stack else False
        
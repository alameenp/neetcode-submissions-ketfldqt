from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            if token in {"*","-","+","/"} :
                a = int(stack.pop())
                b = int(stack.pop())
                if token == "*":
                    out = b*a
                elif token == "-":
                    out = b - a
                elif token == "+":
                    out = b + a
                else:
                    out = int(b/a)
                stack.append(out)
                continue
            stack.append(int(token))
        return stack.pop()


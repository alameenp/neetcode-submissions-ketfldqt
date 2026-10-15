from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        ops = {
            "+": lambda x, y: x+y,
            "-": lambda x, y: x-y,
            "*": lambda x, y: x*y,
            "/": lambda x, y: int(x/y)
        }
        for token in tokens:
            if token in {"*","-","+","/"} :
                a = stack.pop()
                b = stack.pop()
                stack.append(ops[token](b,a))

            else:
                stack.append(int(token))
        return stack.pop()


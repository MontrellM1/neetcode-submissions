class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        ops = {"*", "-", "/", "+"}
    
        for tok in tokens:
            if tok not in ops:
                stack.append(tok)
                continue
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                if tok == "-":
                    stack.append(first - second)
                elif tok == "+":
                    stack.append(first + second)
                elif tok == "/":
                    stack.append(int(first / second))
                elif tok == "*":
                    stack.append(first * second)
        return int(stack[-1])
            

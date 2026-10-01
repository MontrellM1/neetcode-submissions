class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        ops = {"*", "-", "/", "+"}
        if len(tokens) == 1:
            return int(tokens[0])
    
        for tok in tokens:
            if tok not in ops:
                stack.append(tok)
                continue
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                if tok == "-":
                    stack.append(first - second)
                if tok == "+":
                    stack.append(first + second)
                if tok == "/":
                    stack.append(int(first / second))
                if tok == "*":
                    stack.append(first * second)
        return stack[-1]
            

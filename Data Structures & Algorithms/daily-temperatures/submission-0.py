class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                popped = stack.pop()
                wait = i - popped[1]
                result[popped[1]] = wait
            stack.append((temp,i))
        return result
            

        
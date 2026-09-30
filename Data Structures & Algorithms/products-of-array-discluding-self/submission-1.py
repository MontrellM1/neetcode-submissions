import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = []
        runLeft = 1
        right = []
        runRight = 1
        output = []

        for i in range(len(nums)):
            left.append(runLeft)
            runLeft *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            right.append(runRight)
            runRight *= nums[i]

        right.reverse()
        
        for i in range(len(nums)):
            product = right[i] * left[i]
            output.append(product)
        return output


        
        

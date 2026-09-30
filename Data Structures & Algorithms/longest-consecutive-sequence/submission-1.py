class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set()
        numSet = set(nums)
        count = 0

        for num in nums:
            if num - 1 not in numSet:
                current = num
                currentStreak = 1

                while current + 1 in numSet:
                    current += 1
                    currentStreak += 1
            
                if currentStreak > count:
                    count = currentStreak
        return count



        
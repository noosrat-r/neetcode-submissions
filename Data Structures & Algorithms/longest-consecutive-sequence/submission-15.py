class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        res = 0

        for n in nums:
            if n - 1 not in nums:
                localStreakLength = 0
                while n + localStreakLength in nums:
                    localStreakLength += 1
                
                res = max(res, localStreakLength)
        
        return res


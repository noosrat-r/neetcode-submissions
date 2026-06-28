class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()
        res = 0

        expectedCurr = nums[0]
        i = 0
        tempStreak = 0
        while i < len(nums):
            if expectedCurr != nums[i]:
                expectedCurr = nums[i]
                tempStreak = 0

            while i < len(nums) and nums[i] == expectedCurr:
                i += 1
            
            tempStreak += 1
            expectedCurr += 1
            res = max(res, tempStreak)

        return res
        





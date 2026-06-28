class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        for i,n in enumerate(nums):
            temp = 0
            cur = n
            while cur in nums:
                cur += 1
                temp += 1
            res = max(temp, res)

        return res
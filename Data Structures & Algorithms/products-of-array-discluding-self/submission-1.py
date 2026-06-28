class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        for n in nums:
            if n:
                product = product * n
            else:
                zeros += 1
        res = [0] * len(nums)
        if zeros > 1: return res

        for i in range(len(nums)):
            if zeros: res[i] = 0 if nums[i] else product
            else: res[i] = product // nums[i]

        return res
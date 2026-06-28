class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in found:
                return [found[diff], i]
            
            found[n] = i
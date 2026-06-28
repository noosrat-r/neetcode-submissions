class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        nums.sort()

        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            for j in range(i+1, len(nums)):
                count[nums[j]] -= 1

                if j-1 > i and nums[j-1] == nums[j]:
                    continue

                target = -1 * (nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])
                
            for j in range(i+1, len(nums)):
                count[nums[j]] += 1

        return res
                    

                
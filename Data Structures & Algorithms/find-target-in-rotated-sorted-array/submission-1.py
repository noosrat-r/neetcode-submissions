class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # res = -1
        # for i,n in enumerate(nums):
        #     if n == target:
        #         res = i
        
        # return res

        l = 0
        r = len(nums) - 1

        # look for the "pivot" aka the first number in the original sorted array
        # rotated array is just two sorted arrays 
        # it makes sense for l to become the pivot since the pivot is the *first* elemment of the original array
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]: # this is the case where the pivot is on the right side
                l = m + 1
            else: # case where pivot is on the right side, can kind of think of this as a "normal" case?
                r = m 
        
        # check to see which side of the pivot we should actually check
        pivot = l
        l = 0
        r = len(nums) - 1

        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1
        
        # regular binary search
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # trivial, O(N)

        # res = float('inf')

        # for n in nums:
        #     res = min(res,n)
        
        # return res

        # Notes:
        # Array length *n* originally *sorted* in ascending order
        # Input is the sorted array rotated some # of times (r)
        # Little hint where rotating r times moves the last r elements of the array to the beginning

        # should we find r? 
        # feel like this is a binary search problem but how to apply the template here? 
        # i think we can eliminate "fixing" the array because that would cost O(N) when we need O(logN)

        # minimum is really just the first element in the original array
        # maybe we can start l = 0, r = len(nums) - 1 
        # calculate mid and see where mid is compared to l and r ? 

        # two main cases 
        # if nums[l] > nums[r] -> array is sorted
        #   # if nums[mid] > nums[r]
        #       move to the right    
        #   # if nums[mid] < nums[l]
        #       move to the left 
        # else -> array is not sorted
        #   move to the right

        l = 0
        r = len(nums) - 1
        res = float('inf')
        while l <= r:
            mid = l + (r-l)//2

            if nums[l] > nums[r]:
                if nums[mid] > nums[r]:
                    l = mid + 1
                elif nums[mid] < nums[l]:
                    r = mid - 1
            else:
                r = mid - 1
            
            res = min(res, nums[mid])
        
        return res
        

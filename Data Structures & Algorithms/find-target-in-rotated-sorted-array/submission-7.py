class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # res = -1
        # for i,n in enumerate(nums):
        #     if n == target:
        #         res = i
        
        # return res

        l = 0
        r = len(nums)-1

        i = 0
        while l <= r:

            print("*****************************")
            print(f"l : {l}")
            m = l + (r-l)//2
            print(f"m : {m}")
            print(f"r : {r}")

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                print("left side sorted")
                if target > nums[m] or target < nums[l]:
                    print("target is on the right side, moving left pointer")
                    l = m + 1
                else:
                    print("target is on the left side, moving right pointer")
                    r = m - 1
            else:
                print("right side sorted")
                if target < nums[m] or target > nums[r]:
                    print("target is on the left side, moving right pointer")
                    r = m - 1
                else:
                    print("target is on the right side, moving left pointer")
                    l = m + 1
            
            print("new r and l:")
            print(f"l : {l}")
            print(f"r : {r}")

        return -1

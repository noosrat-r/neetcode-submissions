class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()

        for n in nums:
            if n in unique:
                print(n)
                return True
            
            unique.add(n)

        return False
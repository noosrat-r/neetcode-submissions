class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers is sorted increasing
        # return index pair [index1, index2] where index1 > index 2 (1-indexed)
        # only one valid solution

        # index1 > index2 requirement heavily suggests that the solution can be found keeping
        # the array sorted

        # must use O(1) additional space 

        # ince the array is sorted then we know that the target is always going to be after or on index2
        # because nums[index1] + nums[index2] > nums[index2] > nums[index1]

        # [0,1,1,2,3,5,6] target = 1
        # target = nums[index1] + nums[index2]
        # target - nums[index1] = nums[index2]
        # nums[index1] = 0
        # 1 - 0 = 1 so need to look for 1 ahead of index1 without rescanning everything or saving any information
        
        # brute force would be for each number to check all other numbers with the formula above O(n^2)
        
        for i in range(len(numbers)-1):
            find =  target - numbers[i]
            # goal is to eliminate this inner check w/ no extra space
            for j in range(i+1, len(numbers)):
                if numbers[j] == find:
                    return [i+1, j+1]
        
        return []


        

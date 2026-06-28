class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers is sorted increasing
        # return index pair [index1, index2] where index1 > index 2 (1-indexed)
        # only one valid solution

        # index1 > index2 requirement heavily suggests that the solution can be found keeping
        # the array sorted

        # must use O(1) additional space 

        # ince the array is sorted then we know that the target is always going to be after or on index2
        # because numbers[index1] + numbers[index2] > numbers[index2] > numbers[index1]

        # [0,1,1,2,3,5,6] target = 1
        # target = numbers[index1] + numbers[index2]
        # target - numbers[index1] = numbers[index2]
        # numbers[index1] = 0
        # 1 - 0 = 1 so need to look for 1 ahead of index1 without rescanning everything or saving any information
        
        # brute force would be for each number to check all other numbers with the formula above O(n^2)
        
        # missed a very important point -> ** THERE IS ONLY ONE VALID SOLUTION **
        l = 0
        r = len(numbers)-1

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum == target:
                return [l+1, r+1]
            elif sum < target:
                l += 1
            else:
                r -= 1

        return []


        

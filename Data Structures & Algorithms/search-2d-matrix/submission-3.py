class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m x n 2D array - matrix
        # integer - target
    
        # each row is sorted in increasing order 
        # first integer of row > last integer of prev row
        # return true if target exists or false if does not exist

        # aim for O(log(m*n))

        # brute force is O(m*n) checking each row & each column 

        # m = len(matrix)
        # n = len(matrix[0])

        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == target:
        #             return True

        # return False
        
        # O(m + n)
        # m = len(matrix) 
        # n = len(matrix[0])

        # r = 0
        # c = n - 1
        # while r < m and c >= 0:
        #     if matrix[r][c] < target:
        #         r += 1
        #     elif matrix[r][c] > target:
        #         c -= 1
        #     else:
        #         return True
        
        # return False

        rows = len(matrix)
        columns = len(matrix[0])

        l = 0
        r = rows * columns - 1

        while l <= r:
            mid = l + (r-l)//2

            row = mid // columns
            column = mid % columns

            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
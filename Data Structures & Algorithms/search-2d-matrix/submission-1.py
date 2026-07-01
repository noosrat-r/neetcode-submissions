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

        m = len(matrix) 
        n = len(matrix[0])

        r = 0
        c = n - 1
        while r < m and c >= 0:
            if matrix[r][c] < target:
                r += 1
            elif matrix[r][c] > target:
                c -= 1
            else:
                return True
        
        return False
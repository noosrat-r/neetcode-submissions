class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # array of integers representing daily temperature
        # each integer aty integer i = daily temperatures on ith day
        # return result , result[i] = # of days after the ith day before a warmer temperature appears
        # set day to 0 for result[i] if no warmer day exists
        # [30, 38, 30, 36, 35, 40, 28]
        #                      
        # [1, 4, 1, 2, 1, 0, 0]

        # brute force - for each day, scan ahead for a greater number O(N^2)

        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
        
        return res

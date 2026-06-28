class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) 
        stack = [] #contain temperature -> index
        for index, temp in enumerate(temperatures):
            while(stack and temp > stack[-1][0]):
                curIndex = stack.pop()[1]
                res[curIndex] = index - curIndex
            stack.append((temp, index))

        return res


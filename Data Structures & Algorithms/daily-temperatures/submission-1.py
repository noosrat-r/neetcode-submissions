class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) 
        stack = [] #contain temperature -> index
        for index, temp in enumerate(temperatures):
            while(stack and temp > temperatures[stack[-1]]):
                curIndex = stack.pop()
                res[curIndex] = index - curIndex
            stack.append(index)

        return res


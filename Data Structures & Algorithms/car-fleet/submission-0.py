class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        pair = [(c, s) for c,s in zip(position, speed)]
        pair.sort(reverse=True)

        for c,s in pair:
            time = (target-c)/s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)
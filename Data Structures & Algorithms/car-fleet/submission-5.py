class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # must sort to ensure order
        # if not sorted, cant ensure the cars being checked dont have cars inbetween them
        
        # need to make a new array of position,speed pairs
        # go through, ddo a calculation of (position - currPosition) / speed = time

        # can use stack or not
        # cars = [(p,s) for p,s in zip(position,speed)]
        # cars.sort(reverse = True)

        # fleets = 1
        # prevTime = (target-cars[0][0])/cars[0][1]
        # for i in range(1,len(cars)):
        #     currTime = (target-cars[i][0])/cars[i][1]

        #     if currTime > prevTime:
        #         prevTime = currTime
        #         fleets += 1
        # return fleets

        # stack version

        stack = []
        cars = [(p,s) for p,s in zip(position, speed)]
        cars.sort(reverse=True)

        for car in cars:
            time = (target-car[0])/car[1]
            if stack and time <= stack[-1]:
                continue
            stack.append(time)

        return len(stack)
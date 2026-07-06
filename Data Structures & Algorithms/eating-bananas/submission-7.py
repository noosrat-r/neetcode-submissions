class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # this problem has the monotonic property that signals the use of binary search
        # in this case, the monotonic property is not in the array itself but in a range of
        # min k to max k ?

        # brute force 
        # k = 0
        # while(True):
        #     k += 1
        #     hTemp = 0
        #     for p in piles:
        #         hTemp += math.ceil(p/k)

        #     if hTemp <= h:
        #         break
        
        # return k

        # hardest part is figuring out the condition we need to check
        # returning rate, so maybe it has something to do with k
        # we know that k has to be a minimum of 1 
        # maximum of max pile in piles *BUT* it could be less than that
        
        l = 1
        r = max(piles)
        sumOfBananas = sum(piles)
        print(f"sumOfBananas = {sumOfBananas}")
        
        k = 1
        while l <= r:
            midK = l + (r-l)//2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p/midK)

            if totalTime <= h:
                r = midK - 1
                k = midK
            else:
                l = midK + 1
                
        return k
                



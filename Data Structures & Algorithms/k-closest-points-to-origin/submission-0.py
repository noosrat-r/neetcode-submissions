import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointsHeap = []

        x1, y1 = 0,0
        for point in points:
            x2 = point[0]
            y2 = point[1]

            distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            heapq.heappush_max(pointsHeap, [distance, point])

            if len(pointsHeap) > k:
                heapq.heappop_max(pointsHeap)

        res = [point for distance,point in pointsHeap]
        return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for n in nums:
            map[n] += 1

        arr = []
        for num, freq in map.items():
            arr.append([freq, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res
            
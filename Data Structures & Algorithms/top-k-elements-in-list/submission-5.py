class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] += 1

        print(count)

        for num,count in count.items():
            freq[count].append(num)

        res = []
        for f in range(len(freq)-1, 0, -1):
            for num in freq[f]:
                if len(res) == k:
                    break
                res.append(num)
        
        return res

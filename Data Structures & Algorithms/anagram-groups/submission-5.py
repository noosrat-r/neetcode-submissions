class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for s in strs:
            sortedS = "".join(sorted(s))
            map[sortedS].append(s)

        return list(map.values())
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = defaultdict(int)
        for c in s1:
            s1Count[c] += 1

        for l in range(len(s2)):
            tempCount = defaultdict(int)
            for r in range(l, len(s2)):
                if s2[r] not in s1Count:
                    break

                tempCount[s2[r]] += 1
                if tempCount == s1Count:
                    return True

        return False
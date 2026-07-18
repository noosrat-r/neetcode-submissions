class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = defaultdict(int)
        for c in s1:
            s1Count[c] += 1

        need = len(s1Count)
        for l in range(len(s2)):
            tempCount = defaultdict(int)
            curr = 0
            for r in range(l, len(s2)):
                tempCount[s2[r]] += 1
                # if tempCount == s1Count:
                #     return True

                if s1Count[s2[r]] < tempCount[s2[r]]:
                    break
                    
                if s1Count[s2[r]] == tempCount[s2[r]]:
                    curr += 1
                
                if curr == need:
                    return True

        return False
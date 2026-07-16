class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Note: problem specifies upper case english letter which is a hint to use a O(26) array to hold some info

        # loop over every character, then loop over every character after it
        # for every substring, calculate the max frequency
        # only if ( r - l ) - maxfrequency <= k, then calculate the res

        res = 0
        for i in range(len(s)):
            maxfreq = 0
            countMap = defaultdict(int)
            for j in range(i, len(s)):
                countMap[s[j]] += 1
                maxfreq = max(maxfreq, countMap[s[j]])
                if (j - i + 1) - maxfreq <= k:
                    res = max(res, j - i + 1)
        
        return res
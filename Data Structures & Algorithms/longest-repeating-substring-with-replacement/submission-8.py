class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Note: problem specifies upper case english letter which is a hint to use a O(26) array to hold some info

        # loop over every character, then loop over every character after it
        # for every substring, calculate the max frequency
        # only if ( r - l ) - maxfrequency <= k, then calculate the res

        # res = 0
        # for i in range(len(s)):
        #     maxfreq = 0
        #     countMap = defaultdict(int)
        #     for j in range(i, len(s)):
        #         countMap[s[j]] += 1
        #         maxfreq = max(maxfreq, countMap[s[j]])
        #         if (j - i + 1) - maxfreq <= k:
        #             res = max(res, j - i + 1)
        
        # return res

        # res = 0
        # charSet = set(s)
        # for c in charSet:
        #     count = 0
        #     left = 0
        #     for right in range(len(s)):
        #         if s[right] == c:
        #             count += 1
                
        #         while (right-left+1)-count > k:
        #             if s[left] == c:
        #                 count -= 1
                    
        #             left += 1

        #         res = max(res, right-left+1)

        # return res

        res = 0
        l = 0
        freq = defaultdict(int)
        maxFreq = 0
        for r in range(len(s)):
            freq[s[r]] += 1

            maxFreq = max(maxFreq, freq[s[r]])
            while (r-l+1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)

        return res



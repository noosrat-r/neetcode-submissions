class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) == 1:
        #     return 1

        # res = 0
        # for i in range(len(s)-1):
        #     count = 1
        #     for j in range(i+1, len(s)):
        #         if s[j] in s[i:j]:
        #             break
        #         count += 1
        #     res = max(res, count)

        # return res

        res = 0
        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            res = max(res, len(charSet))
        return res
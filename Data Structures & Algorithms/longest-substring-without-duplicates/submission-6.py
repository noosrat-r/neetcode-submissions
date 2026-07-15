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

        l = 0
        r = 0
        charSet = set()
        res = 0
        while r < len(s):
            print("*****************")
            print(f"s[l]: {s[l]}")
            print(f"s[r]: {s[r]}")
            if s[r] in charSet:
                print("duplicate found!")
                while s[r] in charSet:
                    print(f"removing {s[l]}")
                    charSet.remove(s[l])
                    l += 1
            charSet.add(s[r])
            print(f"charSet {charSet}")
            r += 1
            res = max(res, len(charSet))
        return res
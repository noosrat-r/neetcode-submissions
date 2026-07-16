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
        # charSet = set()
        charMap = defaultdict(str)
        res = 0
        # below could just be a simple for loop lol
        # not optimal because of extra O(2N) pass, could be optimal with a hashmap

        # try next time with a hashmap
        while r < len(s):
            print("*****************")
            print(f"s[l]: {s[l]} at l: {l}")
            print(f"s[r]: {s[r]} at r: {r}")
            if s[r] in charMap:
                print("duplicate found!")
                #s[r] could contain index outside of the current substring so take the highest l
                l = max(charMap[s[r]] + 1, l)
            charMap[s[r]] = r
            print(f"charMap {charMap}")
            r += 1
            res = max(res, r-l)
            
        return res
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += f"{length}" + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        print("string: " + s)
        while i < len(s):
            # get index of delimiter
            delimIndex = s.find('#', i)
            # get length of string
            length = int(s[i:delimIndex])
            i = delimIndex + 1
            string = s[i:i+length]

            res.append(string)
            i += length
        return res

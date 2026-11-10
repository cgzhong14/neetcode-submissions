class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res+= str(len(i)) + "#" + i
        return res

    def decode(self, s: str) -> List[str]:
        sLength = len(s)
        i = 0
        res = []
        while i < sLength:
            j = i
            while s[j] != '#':
                j+=1
            # retreive length
            length = int(s[i:j])
            # set boundries
            i = j + 1
            j = i + length
            # add and reset
            res.append(s[i:j])
            i = j
        return res

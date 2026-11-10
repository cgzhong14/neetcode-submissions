class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)
        for i in charSet:
            l = 0
            charCount = 0
            for r in range(len(s)):
                if s[r] == i:
                    charCount+=1
                while (r-l + 1) - charCount > k:
                    if s[l] == i:
                        charCount-=1
                    l+=1
                res = max(res, (r-l + 1))
        return res
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        length = 0
        for i in charSet:
            l = 0
            count = 0
            for r in range(len(s)):
                if s[r] == i:
                    count+=1
                while r-l+1 - count > k:
                    if s[l] == i:
                        count-=1
                    l+=1
                length = max(length, r-l+1)
        return length
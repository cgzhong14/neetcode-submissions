class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        maxC = 0
        for i in s:
            while i in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(i)
            maxC = max(maxC, len(charSet))
        return maxC
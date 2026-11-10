class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        numSet = set()
        seenMax = 0
        l = 0
        for i in range(len(s)):
            while s[i] in numSet:
                numSet.remove(s[l])
                l+=1
            numSet.add(s[i])
            seenMax = max(seenMax,len(numSet))
        return seenMax

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        numSet = set()
        maxCount = 0
        l = 0
        for i in range(len(s)):
            while s[i] in numSet:
                numSet.remove(s[l])
                l+=1
            numSet.add(s[i])
            maxCount = max(maxCount, len(numSet))
        return maxCount
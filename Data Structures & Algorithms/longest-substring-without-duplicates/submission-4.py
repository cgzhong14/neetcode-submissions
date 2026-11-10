class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        numSet = set()
        seenMax = 0
        left = 0
        for i in s:
            while i in numSet:
                numSet.remove(s[left])
                left += 1
            numSet.add(i)
            seenMax = max(seenMax, len(numSet))
        return seenMax
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
            ptr = 0
            for char in t:
                if ptr < len(s) and s[ptr] == char:
                    ptr += 1
            return ptr == len(s)
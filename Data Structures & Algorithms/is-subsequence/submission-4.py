class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False

        ptr1 = 0
        for i in t:
            if s[ptr1] == i:
                ptr1+=1
            if ptr1 == len(s):
                return True
        return ptr1 == len(s)

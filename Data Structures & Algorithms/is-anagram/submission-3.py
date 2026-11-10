class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictionaryS = dict()
        dictionaryT = dict()
        for i in range(len(s)):
            if s[i] not in dictionaryS:
                dictionaryS[s[i]] = 1
            else:
                dictionaryS[s[i]] += 1
            if t[i] not in dictionaryT:
                dictionaryT[t[i]] = 1
            else:
                dictionaryT[t[i]] += 1
        return dictionaryS == dictionaryT

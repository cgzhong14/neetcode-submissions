class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}
        for i in s:
            if i not in dictS:
                dictS[i] = 1
            else:
                dictS[i] += 1
        for j in t:
            if j not in dictT:
                dictT[j] = 1
            else:
                dictT[j] +=1
        return dictT == dictS
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keyDict = {}
        for i in strs:
            sortedKey = "".join(sorted(i))
            if sortedKey not in keyDict:
                keyDict[sortedKey] = [i]
            else:
                keyDict[sortedKey].append(i)

        return list(keyDict.values())
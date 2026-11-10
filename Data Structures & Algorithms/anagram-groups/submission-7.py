class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for i in range(len(strs)):
            sortedString = "".join(sorted(strs[i]))
            if sortedString not in dictionary:
                dictionary[sortedString] = [strs[i]]
            else:
                dictionary[sortedString].append(strs[i])
        return list(dictionary.values())
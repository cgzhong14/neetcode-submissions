class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for i in strs:
            sortedString = "".join(sorted(i))
            if sortedString not in dictionary:
                dictionary[sortedString] = [i]
            else:
                dictionary[sortedString].append(i)
        return list(dictionary.values())
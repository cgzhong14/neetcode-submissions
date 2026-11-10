class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}

        for i in strs:
            sorted_str = "".join(sorted(i))
            if sorted_str in dictionary:
                dictionary[sorted_str].append(i)
            else:
                dictionary[sorted_str] = [i]
        
        return list(dictionary.values())   
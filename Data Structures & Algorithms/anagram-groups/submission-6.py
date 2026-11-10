class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #read the length of the string
        #read the characters of the string
        dictionary = {}
        for word in strs:
            wordToAdd = "".join(sorted(word))
            if wordToAdd not in dictionary:
                dictionary[wordToAdd] = [word]
            else:
                dictionary[wordToAdd].append(word)
        return list(dictionary.values())
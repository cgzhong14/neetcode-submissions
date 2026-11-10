class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stored = {}
        for i in strs:
            z = "".join(sorted(i))
            if z not in stored:
                stored[z]= [i]
            else:
                stored[z].append(i)
        return list(stored.values())
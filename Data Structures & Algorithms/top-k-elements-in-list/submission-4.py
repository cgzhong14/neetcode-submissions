class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for i in nums:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1

        res = []
        for key,v in dictionary.items():
            res.append([v,key])

        res.sort()

        returnArray = []
        for z in range(len(res) -1,-1,-1):
            if len(returnArray) != k:
                returnArray.append(res[z].pop())
            else:
                return returnArray
        return returnArray
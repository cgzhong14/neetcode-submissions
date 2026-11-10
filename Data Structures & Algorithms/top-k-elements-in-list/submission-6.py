class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for i in nums:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        
        values = []
        for key,value in dictionary.items():
            values.append([value,key])
        values.sort()

        returnArray = []
        for z in range(len(values) - 1, -1, -1):
            if len(returnArray) < k:
                returnArray.append(values[z][1])
            else:
                return returnArray
        return returnArray
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kDictionary = {}
        for i in range(len(nums)):
            if nums[i] not in kDictionary:
                kDictionary[nums[i]] = 1
            else:
                kDictionary[nums[i]] += 1

        arr = []
        for key,val in kDictionary.items():
            arr.append([val,key])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

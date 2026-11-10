class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in complementMap:
                return [complementMap[complement], i]
            else:
                complementMap[nums[i]] = i
            # key is number aka compliment
            # if key is in complement
            # then return [currentIndex, complementIndex]
        
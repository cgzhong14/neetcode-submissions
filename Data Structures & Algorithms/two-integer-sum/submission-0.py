class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in compliments:
                return [compliments[complement], i]
            else:
                compliments[nums[i]] = i
        
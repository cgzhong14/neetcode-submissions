class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x = [0] * (len(nums)*2)
        for i in range(len(nums)):
            x[i] = nums[i]
            x[i+len(nums)] = nums[i]
        return x
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter+=1
                maxOnes = max(maxOnes,counter)
            else:
                counter = 0
        return maxOnes
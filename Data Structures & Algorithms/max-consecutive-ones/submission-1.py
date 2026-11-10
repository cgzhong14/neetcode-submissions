class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCounter = 0
        currCount = 0
        for i in nums:
            if i == 1:
                currCount +=1
            else:
                currCount = 0
            maxCounter = max(currCount,maxCounter)
        return maxCounter
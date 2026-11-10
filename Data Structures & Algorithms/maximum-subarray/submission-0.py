class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            #make sure not negative
            curSum = max(curSum,0)
            curSum+=n
            maxSum = max(curSum, maxSum)
        return maxSum
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curSumMax = 0
        curSumMin = 0
        maxSum = nums[0]
        minSum = nums[0]
        total = 0
        for i in nums:
            curSumMax = max(curSumMax, 0) + i
            curSumMin = min(curSumMin, 0) + i
            maxSum = max(maxSum, curSumMax)
            minSum = min(minSum, curSumMin)
            total += i
        if total == minSum:
            return maxSum
        return max(maxSum, total - minSum)
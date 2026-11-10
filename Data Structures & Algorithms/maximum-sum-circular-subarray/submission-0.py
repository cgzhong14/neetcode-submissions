class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        minSum = nums[0]
        curMinSum = 0
        curMaxSum = 0
        total = 0
        for i in nums:
            total+=i
            curMaxSum = max(curMaxSum + i,i)
            curMinSum = min(curMinSum + i,i)
            maxSum = max(maxSum,curMaxSum)
            minSum = min(minSum,curMinSum)
        
        if minSum == total:
            return maxSum
        return max(maxSum, total - minSum)
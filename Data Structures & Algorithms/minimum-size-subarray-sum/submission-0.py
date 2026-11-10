class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        tempTotal = 0
        l = 0
        # create sliding window for variable size
        # keep on increasing the size of window (r)
        # if it exceeds slowly start trimming it from l
        for r in range(len(nums)):
            tempTotal+= nums[r]
            while tempTotal >= target:
                ans = min(ans, r - l + 1)
                tempTotal -= nums[l]
                l += 1

        return ans if ans != float('inf') else 0
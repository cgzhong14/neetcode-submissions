class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        con = set(nums)
        res = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in con:
                j = 0
                while nums[i] + j in con:
                    j+=1
                res = max(res,j)
        return res

        
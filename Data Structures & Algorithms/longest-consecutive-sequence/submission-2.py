class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        counter = 0
        for i in nums:
            if i - 1 not in numSet:
                count = 0
                j = i
                while j in numSet:
                    count+=1
                    j+=1
                counter = max(counter, count)
        return counter 
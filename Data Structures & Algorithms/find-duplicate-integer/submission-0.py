class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        found = set()
        for i in nums:
            if i in found:
                return i
            found.add(i)
        return None
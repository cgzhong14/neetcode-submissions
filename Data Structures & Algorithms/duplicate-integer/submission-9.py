class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateSet = set()
        for i in nums:
            if i not in duplicateSet:
                duplicateSet.add(i)
            else:
                return True
        return False
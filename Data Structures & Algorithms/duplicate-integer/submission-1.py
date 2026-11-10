class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        listt = []
        for i in nums:
            if i not in listt:
                listt.append(i)
            else:
                return True
        return False
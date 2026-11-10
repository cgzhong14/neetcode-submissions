class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited = set()
        k = 0
        for i in nums:
            if i not in visited:
                visited.add(i)
                nums[k] = i
                k += 1
        return k
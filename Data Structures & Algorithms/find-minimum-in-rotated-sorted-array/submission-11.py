class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minimum = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                minimum = min(minimum, nums[l])
                break
            mid = (l+r) // 2
            minimum = min(minimum, nums[mid])
            if nums[mid] >= nums[l]:
                l+=1
            else:
                r-=1
        return minimum        

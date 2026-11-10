class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr1 = 0
        ptr2 = len(nums) - 1

        while ptr1 <= ptr2:
            if nums[ptr1] == val:
                nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
                ptr2 -= 1  # shrink valid end
            else:
                ptr1 += 1  # valid, move on
        
        return ptr1  # new length, all valid elements are in nums[:ptr1]

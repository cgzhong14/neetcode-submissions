class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # L = 0
        # R = 1
        # while R != len(nums):
        #     if nums[R] != val:
        #         nums[L] = nums[R]
        #         L+=1
        #     R+=1
        # return L
        L = 0
        for R in range(len(nums)):
            if nums[R] != val:
                nums[L] = nums[R]
                L += 1
        return L
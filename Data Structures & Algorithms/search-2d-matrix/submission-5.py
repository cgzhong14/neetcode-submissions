class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in matrix:
            if r[0] <= target <= r[-1]:
                return self.binarySearch(r,target)
        return False
    
    def binarySearch(self,row,target):
        l = 0
        r = len(row) - 1
        while l <= r:
            mid = (l+r) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
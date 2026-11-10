class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find the correct row
        for r in matrix:
            if r[0] <= target <= r[-1]:
                return self.binarySearch(r, target)
        return False

    def binarySearch(self, row, target):
        lower = 0
        upper = len(row) - 1
        
        while lower <= upper:
            mid = (lower + upper) // 2
            if row[mid] < target:
                lower = mid + 1
            elif row[mid] > target:
                upper = mid - 1
            else:
                return True
        return False

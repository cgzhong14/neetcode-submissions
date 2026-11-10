class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        newArray = [0] * len(arr)
        rightMax = -1
        for i in range(len(arr)-1, 0,-1):
            newArray[i] = rightMax
            rightMax = max(arr[i], rightMax)
        newArray[0] = rightMax
        return newArray
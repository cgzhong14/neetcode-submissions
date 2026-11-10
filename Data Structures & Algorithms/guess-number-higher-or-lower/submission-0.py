class Solution:
    def guessNumber(self, n: int) -> int:
        # since in problem it says 1 to n. Start at 1.
        l = 1
        r = n
        while l < r:
            mid = (l+r) // 2
            guessAPI = guess(mid)
            if guessAPI == 0:
                return mid
            elif guessAPI == -1:
                r= mid -1
            else:
                l = mid+1
        return l

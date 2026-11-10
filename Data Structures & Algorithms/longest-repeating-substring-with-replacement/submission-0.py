class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)
        for c in charSet:          # Try making the whole window each unique char
            count = l = 0
            for r in range(len(s)): # r = right edge of window, expands every iteration
                if s[r] == c:
                    count += 1     # Track how many c's are in the current window

                while r - l + 1 - count > k:  # Too many replacements needed?
                    if s[l] == c:
                        count -= 1 # Losing a c as we shrink from the left
                    l += 1         # Shrink window from the left

                res = max(res, r - l + 1)  # Valid window — record its size
        return res
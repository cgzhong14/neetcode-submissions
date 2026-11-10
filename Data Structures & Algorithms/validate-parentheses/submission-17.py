class Solution:
    def isValid(self, s: str) -> bool:
        dictionary= {'}': '{', ']':'[', ')':'('}
        stack = []
        for i in s:
            if i in dictionary:
                if not stack or stack[-1] != dictionary[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0
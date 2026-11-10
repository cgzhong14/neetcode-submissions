class Solution:
    def isValid(self, s: str) -> bool:
        parent = {')':'(', '}':'{', ']':'['}
        stack = []
        for i in s:
            if i in parent:
                if not stack or stack[-1] != parent[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0 
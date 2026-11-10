class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis = {'}':'{',')':'(',']':'['}
        stack = []
        for i in s:
            if i in paranthesis:
                if not stack or stack[-1] != paranthesis[i]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0

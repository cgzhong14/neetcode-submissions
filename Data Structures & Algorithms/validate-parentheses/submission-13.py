class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        myStack = []
        for i in range(len(s)):
            if s[i] == ']' or s[i] == ')' or s[i] == '}':
                if len(myStack) == 0:
                    return False
                otherChar = myStack.pop()
                if s[i] == ']' and otherChar != '[':
                    return False
                elif s[i] == ')' and otherChar != '(':
                    return False
                elif s[i] == '}' and otherChar != '{':
                    return False
            else:
                myStack.append(s[i])
        return len(myStack) == 0
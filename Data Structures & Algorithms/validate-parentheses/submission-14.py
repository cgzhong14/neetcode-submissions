class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []
        
        # Map closing brackets to their corresponding opening brackets
        matching = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            if char in matching:  # It's a closing bracket
                # Check if stack is empty or top doesn't match
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()
            else:  # It's an opening bracket
                stack.append(char)
        
        # Valid only if all brackets were matched (stack is empty)
        return len(stack) == 0
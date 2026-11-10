class Solution:
    def isValid(self, s: str) -> bool:
        parantheses = {')':'(', '}':'{', ']':'['}
        arr = []
        for i in s:
            if i not in parantheses:
                arr.append(i)
            else:
                if not arr or arr[-1] != parantheses[i]:
                    return False
                else:
                    arr.pop()
        
        return len(arr) == 0
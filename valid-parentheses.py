class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matching_bracket = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in matching_bracket.values():
               
                stack.append(char)
            elif char in matching_bracket.keys():
               
                if len(stack) == 0 or stack.pop() != matching_bracket[char]:
                    return False
  

        return len(stack) == 0

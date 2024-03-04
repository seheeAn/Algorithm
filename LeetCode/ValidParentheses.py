class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['{','[','(']:
                stack.append(c)
            else:
                if not stack:
                    return False

                if c == ")" and stack.pop() != "(":
                    return False
                elif c == "}" and stack.pop() != "{":
                    return False
                elif c == "]" and stack.pop() != "[":
                    return False
        
        return len(stack) == 0

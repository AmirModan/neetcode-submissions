class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in "({[":
                stack.append(p)
            else:
                if stack:
                    opening = stack.pop()
                    if (opening == '(' and p != ')') or (opening == '[' and p != ']') or (opening == '{' and p != '}'):
                        return False
                else:
                    return False
        return not stack
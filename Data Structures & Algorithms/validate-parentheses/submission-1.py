class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        close_to_open ={
            ")":"(",
            "}":"{",
            "]":"["
        }

        for i in range(len(s)):
            if s[i] not in close_to_open:
                stack.append(s[i])
            elif s[i] in close_to_open and stack and close_to_open[s[i]]==stack[-1]:
                stack.pop()
            else:
                return False

        return True if not stack else False

        
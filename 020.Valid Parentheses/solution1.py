class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_parenthesis = ["(", "[", "{"]
        close_parenthesis = [")", "]", "}"]
        for _, elem in enumerate(s):

            if elem in open_parenthesis:
                stack.append(elem)
            elif elem in close_parenthesis:
                if len(stack) == 0:
                    return False
                if close_parenthesis.index(elem) != open_parenthesis.index(stack[-1]):
                    return False
                stack.pop(-1)

        if len(stack) == 0:
            return True





s = "()[]{}"
sol = Solution()
ret = sol.isValid(s)
print(ret)
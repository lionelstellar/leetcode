"""
最长有效括号序列：
栈顶记录下上一个close括号的index，默认为-1，后续出栈的close序号与之作差就是长度
遇到open就push，遇到close就pop，pop时判断一下要不要把空栈补最后一个close
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        result = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    result = max(result, (i - stack[-1]))

        return result

sol = Solution()
str=")()()(())"

print(sol.longestValidParentheses(str))


"""
"""
class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        def justify(line):
            words = line.split(" ")
            if len(words) == 1:
                return line + " " * (maxWidth - len(line))

            space_len = maxWidth - len("".join(words))
            space_num = len(words) - 1
            base_len = space_len // space_num
            padding = space_len % space_num

            space = [" " * base_len] * space_num
            for i in range(padding):
                space[i] += " "

            justify_line = ""
            for i in range(space_num):
                justify_line += words[i] + space[i]
            justify_line += words[space_num]
            return justify_line


        i = 0
        res = []
        line = ""
        while i < len(words):
            if len(line) + len(words[i]) + 1 <= maxWidth + 1:
                line += " " + words[i]
            else:
                res.append(justify(line.lstrip()))
                line = " " + words[i]
            i += 1

        if line:
            res.append(line.lstrip() + " " * (maxWidth - len(line.lstrip())))

        return res


sol = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(sol.fullJustify(words, maxWidth))
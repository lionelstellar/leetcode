class Solution:
    def countAndSay(self, n: int) -> str:
        def generate_next(s: str)-> str:
            ch = ""
            count = 0
            i = 0
            ret = ""
            while i < len(s):
                if ch != s[i]:
                    if count > 0:
                        ret += str(count) + ch
                    ch = s[i]
                    count = 1
                else:
                    count += 1

                i += 1
            ret += str(count) + ch
            return ret


        i = 1
        s = "1"
        while i < n:
            s = generate_next(s)
            i += 1

        return s




sol = Solution()
num = 5
print(sol.countAndSay(num))
class Solution:

    def intToRoman(self, num: int) -> str:
        ret_str = self.parse(num // 1000, 1000) + \
                    self.parse(num%1000//100, 100) + \
                    self.parse(num%100//10, 10) +\
                    self.parse(num%10, 1)
        return ret_str

    def parse(self, num, base):
        dict = {1: ["I", "V"], 10: ["X", "L"], 100: ["C", "D"], 1000: ["M"]}
        # 0 <= num <= 9
        if num <= 3:
            ret = dict[base][0] * num

        elif num == 4:
            ret = dict[base][0] + dict[base][1]
        elif num <= 8:
            ret = dict[base][1] + dict[base][0] * (num - 5)
        else:
            ret = dict[base][0] + dict[base * 10][0]
        return ret

sol = Solution()
num = 1998
print(sol.intToRoman(num))


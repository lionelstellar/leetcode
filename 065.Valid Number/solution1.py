"""
"""
class Solution:
    def isNumber(self, s: str) -> bool:
        def isNumberDigit(ch):
            if len(ch) == 1 and "0" <= ch <= "9":
                return True
            else:
                return False

        def isSign(ch):
            if len(ch) == 1 and ch in ["+", "-"]:
                return True
            else:
                return False

        def isFloat(s):
            if s.count(".") != 1:
                return False
            # if s == ".":
            #     return True

            if len(s) == 1 or s in ["+.", "-."]:
                return False

            int_str, pure_float_str = s.split(".")
            int_flag = False

            if len(int_str) == 0:
                int_flag = True
            elif len(int_str) == 1:
                if isNumberDigit(int_str) or isSign(int_str):
                    int_flag = True
            else:
                int_flag = isInt(int_str)

            pure_float_flag = True
            if len(pure_float_str) == 0:
                pure_float_flag = True
            elif len(pure_float_str) > 0:
                for ch in pure_float_str:
                    if not isNumberDigit(ch):
                        pure_float_flag = False
            else:
                pure_float_flag = False
            return int_flag and pure_float_flag

        def isInt(s):
            if len(s) == 0:
                return False
            elif len(s) == 1:
                return isNumberDigit(s[0])
            else:
                if isSign(s[0]) or isNumberDigit(s[0]):
                    for i in range(1, len(s)):
                        if not isNumberDigit(s[i]):
                            return False
                    return True
                else:
                    return False



        if s.count("e") + s.count("E") > 1:
            return False
        elif s.count("e") + s.count("E") == 0:
            a = isFloat(s)
            b = isInt(s)
            return isFloat(s) or isInt(s)
        else:
            if "e" in s:
                ch = "e"
            else:
                ch = "E"
            before, after = s.split(ch)

        return (isFloat(before) or isInt(before)) and isInt(after)


sol = Solution()
s = ".1"
print(sol.isNumber(s))
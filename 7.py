class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 除去空格
        s = str(x)

        if s == '':
            return 0

        # 判断正负
        flag = 1
        if s[0] == '-':
            flag = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        num = 0
        s = s[len(s)::-1]
        overflow = 0
        for digit in s:
            if num >= 2147483647 and flag == 1:
                return 0
            elif num >= 2147483648 and flag == -1:
                return 0
            elif not '0' <= digit <= '9':
                if flag == 1:
                    return num
                else:
                    return -1 * num
            else:
                num = num * 10 + int(digit)

        if num >= 2147483647 and flag == 1:
            return 0
        elif num >= 2147483648 and flag == -1:
            return 0

        if flag == 1:
            return num
        else:
            return -1 * num



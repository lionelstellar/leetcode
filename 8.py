class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # 除去空格
        str = str.strip(' ')

        if str == '':
            return 0

        # 判断正负
        flag = 1
        if str[0] == '-':
            flag = -1
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]


        num = 0

        overflow = 0
        for digit in str:
            if num >= 2147483647 and flag == 1:
                    return 2147483647
            elif num >= 2147483648 and flag == -1:
                    return -2147483648
            elif not '0' <= digit <= '9':
                if flag == 1:
                    return num
                else:
                    return -1 * num
            else:
                num = num * 10 + int(digit)

        if num >= 2147483647 and flag == 1:
            return 2147483647
        elif num >= 2147483648 and flag == -1:
            return -2147483648

        if flag == 1:
            return num
        else:
            return -1 * num

s=Solution()
print(s.myAtoi('-2147483647'))
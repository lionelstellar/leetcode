class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letter_dict = {"2": "abc", "3": "def", "4": "ghi", \
                       "5": "jkl", "6": "mno", "7": "pqrs", \
                       "8": "tuv", "9": "wxyz"}

        ret = [""]
        for elem in digits:
            tmp = []
            for letter in letter_dict[elem]:
                if ret[-1] != "":
                    for string in ret[-1]:
                        tmp.append(string + letter)
                else:
                    tmp.append(letter)
            tmp.sort()
            ret.append(tmp)
        return ret[-1]


sol = Solution()
digits = "23"
print(sol.letterCombinations(digits))
#Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]






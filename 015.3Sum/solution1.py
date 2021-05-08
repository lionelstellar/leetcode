class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ret = []
        nums.sort()
        for i in range(len(nums) -2):
            two_sum = ~(nums[i]) + 1
            start = i + 1
            end = len(nums) - 1
            while start < end:
                tmp_sum = nums[start] + nums[end]
                if tmp_sum == two_sum:
                    three_sum_set = [nums[i], nums[start], nums[end]]
                    if three_sum_set not in ret:
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

                        ret.append(three_sum_set)
                    start += 1
                    end -= 1
                elif tmp_sum > two_sum:
                    end -= 1
                else:
                    start += 1
        return ret

sol = Solution()
nums = [-1,0,1,2,-1,-4]
#nums = [0]
print(sol.threeSum(nums))







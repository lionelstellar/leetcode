"""
遍历nums，将当前数插入前面所有的permutaion list的各个位置，组成新的permutation set，直到所有数都插入
"""
import copy
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        ret = [[nums[0]]]
        for index in range(1, len(nums)):
            new_ret = []
            for sub_list in ret:
                for insert_place in range(0, index + 1):
                    tmp = copy.deepcopy(sub_list)
                    tmp.insert(insert_place, nums[index])
                    new_ret.append(tmp)

            ret = new_ret
        return ret

sol = Solution()
nums = [1,2,3,4]
print(sol.permute(nums))
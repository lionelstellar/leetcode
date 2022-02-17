"""
暴力搜索头尾逼近
"""
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] < target:
                i += 1
            elif nums[i] == target:
                return i
            else:
                break

        while i <= j:
            if nums[j] > target:
                j -= 1
            elif nums[j] == target:
                return j
            else:
                break

        return -1
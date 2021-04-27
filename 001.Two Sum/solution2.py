# use a dict
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        d = {}
        ret = []
        for i, num in enumerate(nums):
            if target - num in d:
                ret.append(d[target - num])
                ret.append(i)
                return ret
            d[num] = i
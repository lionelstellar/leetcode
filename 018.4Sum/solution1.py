class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        def threeSum(nums: list[int], target) -> list[list[int]]:
            lookup = {}
            res = set()

            nums.sort()

            # last index for each of the elements in nums
            for i, each in enumerate(nums):
                lookup[each] = i

            for i, a in enumerate(nums):
                if i != 0 and nums[i] == nums[i - 1]:
                    continue
                for j, b in enumerate(nums[i + 1:]):
                    c = target - a - b
                    if c in lookup and lookup[c] > j + i + 1:
                        res.add((a, b, c))

            return list(res)

        ret = set()
        pickout = ""
        nums.sort()
        for index, elem in enumerate(nums):
            if pickout != elem:
                nums.remove(elem)
                res = threeSum(nums, target - elem)
                nums.insert(index, elem)
                pickout = elem

                if res:
                    for three_sum_ret in res:
                        four_sum_set = [three_sum_ret[0], three_sum_ret[1], three_sum_ret[2], elem]
                        four_sum_set.sort()
                        ret.add((four_sum_set[0], four_sum_set[1], four_sum_set[2], four_sum_set[3]))

        return list(ret)

sol = Solution()
nums = [1,0,-1,0,-2,2]
target = 0
print(sol.fourSum(nums, target))
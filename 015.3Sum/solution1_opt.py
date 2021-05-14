class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        lookup = {}
        min_distance = 43000
        sum = 0
        for i, elem in enumerate(nums):
            lookup[elem] = i

        for i, a in enumerate(nums):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j, b in enumerate(nums[i + 1:]):
                for c in lookup:

                    if abs(a+b+c-target) < min_distance and lookup[c] > i + j + 1:
                        sum = a+b+c
                        min_distance = abs(a+b+c-target)
                        if min_distance == 0:
                            return sum

        return sum



sol = Solution()
nums = [1,1,1,0]
target = -100

print(sol.threeSumClosest(nums, target))







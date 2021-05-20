class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        # divide and conquer
        def kSum(nums: list[int], target: int, k) -> list[list[int]]:

            # no solution, return null
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return []

            # use twoSum when k is two
            if k == 2:
                return twoSum(nums, target)

            # when k > 2, pickout one number and try add it to list in ksum([elem | elem > number], target - number, k - 1)
            # turn a k problem into a k-1 problem
            res = []
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for _, res_k_minus_1_elem in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                        res.append([nums[i]] + res_k_minus_1_elem)
            return res

        def twoSum(nums: list[int], target: int) -> list[list[int]]:
            res = []
            s = set()
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s.add(nums[i])
            return res

        nums.sort()
        return kSum(nums, target, 4)

sol = Solution()
nums = [1,0,-1,0,-2,2]
target = 0
print(sol.fourSum(nums, target))
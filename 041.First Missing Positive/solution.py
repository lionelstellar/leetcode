class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        def swap(a: int, b: int, nums: list):
            tmp = nums[a]
            nums[a] = nums[b]
            nums[b] = tmp

        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                swap(i, nums[i] - 1, nums)

        for i ,elem in enumerate(nums):
            if elem != i + 1:
                return i + 1

        return len(nums) + 1


sol = Solution()
nums = [1,7,8,9,3,2]
nums = [1]
print(sol.firstMissingPositive(nums))
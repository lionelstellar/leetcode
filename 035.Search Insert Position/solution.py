class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return i + 1

nums = [1, 3, 5, 6]
target = 7
sol = Solution()
print(sol.searchInsert(nums, target))

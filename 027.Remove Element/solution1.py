class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        cur = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[cur] = nums[i]
                cur += 1

        nums = nums[0:cur]
        # print(nums)
        return cur


nums = [0,1,2,2,3,0,4,2]
val = 2
sol = Solution()
print(sol.removeElement(nums, val))
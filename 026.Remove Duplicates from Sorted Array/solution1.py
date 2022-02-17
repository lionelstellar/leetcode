class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        cur = ""
        res_len = -1
        for i in range(len(nums)):
            if nums[i] == cur:
                continue
            else:
                cur = nums[i]
                res_len += 1
                nums[res_len] = cur

        return res_len + 1



nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
print(sol.removeDuplicates(nums))


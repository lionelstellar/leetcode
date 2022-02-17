class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        s=set(nums)
        nums.clear()
        for i in s:
            nums.append(i)
        nums.sort()
        return(len(nums))

nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
print(sol.removeDuplicates(nums))
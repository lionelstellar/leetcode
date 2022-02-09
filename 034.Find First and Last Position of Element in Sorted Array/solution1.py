class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        low = 0
        high = len(nums) - 1
        mid = -1
        while low <= high:
            mid = (low + high) // 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                break

        if mid == -1 or nums[mid] != target:
            return [-1, -1]

        low = high = mid

        while low >= 0 and nums[low] == target:
            low -= 1

        while high <= len(nums) - 1 and nums[high] == target:
            high += 1
        return [low + 1, high - 1]


sol=Solution()
nums=[]

print(sol.searchRange(nums, 10))







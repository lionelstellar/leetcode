"""
二分法找到pivot，再对2个递增区间分别二分查找
"""
class Solution:
    def search(self, nums: list[int], target: int) -> int:

        def find_pivot(nums) -> int:
            if nums[0] < nums[-1] or len(nums) == 1:
                return len(nums)
            mid = len(nums) // 2

            if nums[0] < nums[mid]:
                return mid + find_pivot(nums[mid:])
            else:
                return find_pivot(nums[0: mid])

        def bin_search(nums, left, right, target) -> int:
            if left > right:
                return -1

            if left == right:
                if nums[left] == target:
                    return left
                else:
                    return -1
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return bin_search(nums, left, mid, target)
            else:
                return bin_search(nums, mid + 1, right, target)

        length = len(nums)
        left = 0
        right = len(nums)
        pivot = 0

        if length == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        else:
            if nums[0] < nums[-1] or len(nums) == 1:
                pivot = 0
            else:
                pivot = find_pivot(nums)

            index1 = bin_search(nums, 0, pivot - 1, target)
            index2 = bin_search(nums, pivot, length - 1, target)

            if index1 == -1 and index2 == -1:
                return -1

            if index1 != -1:
                return index1
            else:
                return index2





sol=Solution()
nums=[4,5,6,7,0,1,2]

print(sol.search(nums, 0))
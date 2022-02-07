class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = 0
        while i < length - 1:
            if nums[length - 1 - i] <= nums[length - 2 - i]:
                i += 1
            else:
                break

        p = length - i - 1
        q = length - 1
        while p < q:
            tmp = nums[p]
            nums[p] = nums[q]
            nums[q] = tmp
            p += 1
            q -= 1

        if i < length - 1:
            target = nums[length - i - 2]
            for j in range(length - i - 1, length):
                if nums[j] > target:
                    nums[length - i - 2] = nums[j]
                    nums[j] = target
                    break

        print(nums)



sol = Solution()
nums = [10, 9, 8, 7]

sol.nextPermutation(nums)
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:

        n = len(nums)
        if n == 3:
            return nums[0] + nums[1] + nums[2]

        nums.sort()

        # initial the result
        v = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):

            # compare first, if the largest value we can get is still smaller than target

            s = nums[i] + nums[n - 2] + nums[n - 1]

            if s == target:
                return s
            if s < target:

                # we can skip the two-point at this i value, since two-point let the value increase steply
                if abs(s - target) < abs(v - target):
                    v = s
                continue

            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s - target == 0:
                    return target
                elif s - target > 0:
                    k -= 1
                else:
                    j += 1
                if abs(s - target) < abs(v - target):
                    v = s

        return v
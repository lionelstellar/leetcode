class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ret = []
        nums.sort()
        from collections import Counter
        counter = Counter(nums)
        for i in range(len(nums) -2):
            two_sum = ~(nums[i]) + 1
            start = i + 1
            end = len(nums) - 1
            while start < end:
                tmp_sum = nums[start] + nums[end]
                if tmp_sum == two_sum:
                    three_sum_set = [nums[i], nums[start], nums[end]]
                    if three_sum_set not in ret:
                        ret.append(three_sum_set)
                    start += counter.get(nums[start])
                    end -= counter.get(nums[end])
                elif tmp_sum > two_sum:
                    end -= counter.get(nums[end])
                else:
                    start += counter.get(nums[start])
        return ret

sol = Solution()
nums = [-1,0,1,2,-1,-4]
#nums = [0]
print(sol.threeSum(nums))







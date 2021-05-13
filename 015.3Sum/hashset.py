class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        lookup = {}
        res = set()

        nums.sort()

        # last index for each of the elements in nums
        for i, each in enumerate(nums):
            lookup[each] = i


        for i, a in enumerate(nums):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            for j, b in enumerate(nums[i+1:]):
                target = 0-a-b
                if target in lookup and lookup[target] > j+i+1:
                    res.add((a,b,target))

        return list(res)

sol = Solution()
nums = [-1,0,1,2,-1,-4]
#nums = [0]
print(sol.threeSum(nums))

"""
illustration:
1. sort the number list
2. put every number's last index into a dict/hashmap
3. assume a + b + c == 0, a <= b <= c and the indexes of a,b,c are i,j,k repectively
   k > j has to be satisfied.
   do two "for loop" for a and b, just to check if c in dict and index of c is greater than index of b
"""
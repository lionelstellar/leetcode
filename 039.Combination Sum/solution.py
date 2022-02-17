"""
dfs
"""
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur)
                return
            if total > target:
                return
            for j in range(i, len(candidates)):
                dfs(j, cur + [candidates[j]], total + candidates[j])

        dfs(0, [], 0)
        return res





sol = Solution()
candidates = [2, 3, 5]
target = 8
print(sol.combinationSum(candidates, target))
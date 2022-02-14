"""
dfs+剪枝(下一个candidates必须与上一个不同)
"""
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        def dfs(i, cur, total):
            if total == target:
                res.append(cur)
                return
            if total > target:
                return
            prev = -1
            for j in range(i, len(candidates)):
                if candidates[j] == prev:
                    continue
                dfs(j + 1, cur + [candidates[j]], total + candidates[j])
                prev = candidates[j]

        res = []
        candidates.sort()
        dfs(0, [], 0)
        return res





sol = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8

candidates = [1,1,1]
target = 3
print(sol.combinationSum2(candidates, target))
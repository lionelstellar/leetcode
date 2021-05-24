class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ret = []

        def recursion(res, candidates, target):
            for elem in candidates:
                if elem == target:
                    for res_item in res:
                        res_item.append(elem)
                        return res

                elif elem < target:
                    for res_item in res:
                        res_item += recursion(res, candidates, target - elem)



sol = Solution()
candidates = [2, 3, 5]
target = 8
print(sol.combinationSum(candidates, target))
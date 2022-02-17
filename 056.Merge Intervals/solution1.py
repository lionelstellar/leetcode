"""
列表按 列表元素 的首位排序：intervals.sort(key=lambda x:x[0])
"""
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x:x[0])

        merged = []
        for elem in intervals:
            if not merged or merged[-1][1] < elem[0]:
                merged.append(elem)
            else:
                merged[-1][1] = max(merged[-1][1], elem[1])

        return merged


sol = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[4,5],[1,4],[0,1]]
print(sol.merge(intervals))
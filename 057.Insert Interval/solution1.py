"""
插入后利用merge intervals
"""
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not newInterval:
            return intervals
        if not intervals:
            return [newInterval]
        a, b = newInterval

        if a <= intervals[0][0]:
            intervals.insert(0, newInterval)
        elif a >= intervals[-1][0]:
            intervals.append(newInterval)
        else:
            for i in range(1, len(intervals)):
                if intervals[i - 1][0] <= a <= intervals[i][0]:
                    intervals.insert(i, newInterval)
                    break
        merged = []
        for elem in intervals:
            if not merged or merged[-1][1] < elem[0]:
                merged.append(elem)
            else:
                merged[-1][1] = max(merged[-1][1], elem[1])

        return merged



sol = Solution()
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
intervals = [[0,5],[9,12]]
newInterval = [7,16]



print(sol.insert(intervals, newInterval))
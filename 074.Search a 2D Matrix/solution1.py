"""
先二分找出行，再二分从行中找出元素
"""
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        p, q = 0, m - 1
        while p < q - 1:
            mid = (p + q) // 2
            if matrix[mid][0] <= target:
                p = mid
            elif matrix[mid][n - 1] >= target:
                q = mid
            else:
                return False

        l = matrix[p]
        if p != q:
            l += matrix[q]

        r, s = 0, len(l) - 1
        while r < s - 1:
            mid = (r + s) // 2
            if l[mid] == target:
                return True
            elif l[mid] < target:
                r = mid
            elif l[mid] > target:
                s = mid

        if l[r] != target and l[s] != target:
            return False
        else:
            return True





sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

matrix = [[1]]
target = 0
print(sol.searchMatrix(matrix, target))
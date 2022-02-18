"""
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = []
        for elem in path[1:].split("/"):
            if elem == "..":
                if dirs:
                    dirs.pop()
            elif elem == "." or elem == "":
                pass
            else:
                dirs.append(elem)

        return "/" + "/".join(dirs)


sol = Solution()
path = "/a//b////c/d//././/.."
print(sol.simplifyPath(path))
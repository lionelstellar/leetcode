"""
defaultdict可以以list/set等对象作为key
"""

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        table = defaultdict(list)
        for st in strs:
            table["".join(sorted(st))] += [st]
        return [table[x] for x in table]



sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
strs = ["ddddddddddg","dgggggggggg"]
print(sol.groupAnagrams(strs))
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        length = len(words)
        k = []
        g = []
        from itertools import permutations

        a=list(set(permutations(words,length)))
        l1 = len(words) * len(words[0])
        for i in a:
            s1=''.join(i)
            k.append(s1)
        for i in range(0,(len(s)-l1)+1):
            s2=s[i:(l1+i)]
            if s2 in k:
                g.append(i)
        return(g)

sol = Solution()
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
print(sol.findSubstring(s, words))
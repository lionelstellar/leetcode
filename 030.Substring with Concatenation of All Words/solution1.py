class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        def pickout(words, word):
            words.remove(word)
            res = [ elem for elem in words]
            words.append(word)
            return res

        def check(s, words):
            if words == []:
                return True
            else:
                for elem in words:
                    if s.startswith(elem):
                        if check(s[len(elem):], pickout(words, elem)):
                            return True
                return False


        res = []
        max_len = len(words) * len(words[0])
        for i in range(0, len(s) - max_len + 1):
            if check(s[i:], words):
                res.append(i)

        return res



sol = Solution()
s = "wordgoodgoodgoodbestword"



words = ["word","good","best","good"]
print(sol.findSubstring(s, words))
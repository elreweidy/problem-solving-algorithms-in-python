class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x))

        def helper(sub, whole):
            N, M = len(sub), len(whole)
            i, j = 0, 0
            while i < N and j < M:
                if sub[i] == whole[j]:
                    i += 1
                j += 1

            return i == N

        empty = ""
        for w in d:
            if helper(w, s):
                return w
        return empty





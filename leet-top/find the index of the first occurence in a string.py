class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1

        target = len(list(needle))
        for i in range(len(haystack)):
            if needle[0] == haystack[i]:
                t = 1
                temp = i
                if t == target:
                    return temp
                for j in range(len(needle[1:])):
                    if needle[j + 1] == haystack[j + i + 1]:
                        t += 1
                        if t == target:
                            return temp
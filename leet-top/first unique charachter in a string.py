class Solution:
    def firstUniqChar(self, s: str) -> int:
        sl = list(s)
        if len(sl) == 1:
            return 0
        for i in range(len(sl)):
            s2 = s.replace(sl[i], '', 1)
            if sl[i] not in s2:
                return i
            s2 = s
        return -1
from collections import Counter
class Solution:
    def checkRecord(self, s: str) -> bool:
        counts = Counter(s)
        if counts['A'] < 2 and 'LLL' not in s:
            return True
        return False
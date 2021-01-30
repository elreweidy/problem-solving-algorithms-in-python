class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        l1 = ""
        l2 = ""

        for i in word1:
            l1 += i

        for j in word2:
            l2 += j

        if l1 == l2:
            return True
        else:
            return False

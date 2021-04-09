class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        order_with_key = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for k in range(min(len(word1), len(word2))):
                if word1[k] != word2[k]:
                    if order_with_key[word1[k]] > order_with_key[word2[k]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True
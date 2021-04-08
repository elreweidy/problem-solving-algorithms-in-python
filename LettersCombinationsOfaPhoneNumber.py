class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_dict = {'2': 'abc',
                       '3': 'def',
                       '4': 'ghi',
                       '5': 'jkl',
                       '6': 'mno',
                       '7': 'pqrs',
                       '8': 'tuv',
                       '9': 'wxyz'}

        comp = ['']

        if len(digits) == 0:
            return []

        for d in digits:
            tem = []
            for c in digits_dict[d]:
                tem = tem + [r + c for r in comp]

            comp = tem

        return comp
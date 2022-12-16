class Solution:
    def romanToInt(self, s: str) -> int:
        val = 0
        if "IV" in s:
            val += 4
            s = s.replace("IV", '')
        if "IX" in s:
            val += 9
            s = s.replace("IX", '')
        if "XL" in s:
            val += 40
            s = s.replace("XL", '')
        if "XC" in s:
            val += 90
            s = s.replace("XC", '')
        if "CD" in s:
            val+=400
            s = s.replace("CD", '')
        if "CM" in s:
            val+= 900
            s = s.replace("CM", '')

        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M': 1000}
        sl = list(s)

        for c in sl:
            val += romans[c]
        return val
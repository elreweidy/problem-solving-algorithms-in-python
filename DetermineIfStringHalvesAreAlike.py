class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        a = []
        b = []
        a_vowels = 0
        b_vowels = 0

        for i in range(len(s)):
            if i < len(s) / 2:
                a.append(s[i])

            else:
                b.append(s[i])

        for i in range(len(a)):
            if a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u':
                a_vowels += 1
            if b[i] == 'a' or b[i] == 'e' or b[i] == 'i' or b[i] == 'o' or b[i] == 'u':
                b_vowels += 1

        if a_vowels == b_vowels:
            return True
        else:
            return False
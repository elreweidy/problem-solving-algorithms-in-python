class Solution:
    def reverseBits(self, n: int) -> int:
        # convert n to binary
        binary = bin(n).replace("0b", "")

        # convert n to a list --> [nl]
        nl = list(str(binary))

        # fill the rest of the 32 bits with zeros,
        # which should be at the front of nl
        zeros = []
        for i in range(32 - len(nl)):
            zeros.append(0)
        nl = zeros + nl

        # reverse nl
        nl = list(reversed(nl))

        # converting it back to string
        n = ''.join(str(x) for x in nl)

        # returing the decimal number [n]
        return int(n, 2)
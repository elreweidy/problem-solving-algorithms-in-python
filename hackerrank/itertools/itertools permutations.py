# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
import sys
import select

S , k= list(input().split(' '))
S = sorted(S)

if k != None:
    for i in list(permutations(S, int(k))):
        print(''.join(i))

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
S = input()


for k, group in (groupby(S)):
    print(('({}, {})'.format(len(list((group))), k)), end=' ')
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

S, k = list(input().split())

for i in range(1, int(k) + 1):

    for j in list(combinations(sorted(S), i)):
        print(''.join(j))


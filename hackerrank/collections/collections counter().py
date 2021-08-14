# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

X = int(input())
sizes = list(map(int, input().split()))
N = int(input())

Dict = Counter(sizes)

gain = 0

for i in range(N):
    size, price = list(map(int, input().split(' ')))

    if Dict[size]:
        Dict[size] -= 1

        gain += price
print(gain)
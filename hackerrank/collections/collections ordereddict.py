# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

N = int(input())
ordereddict = OrderedDict()

for i in range(N):
    name, space, price = input().rpartition(" ")
    price = int(price)
    if name in ordereddict.keys():

        ordereddict[name] += price

    else:
        ordereddict[name] = price

for i in ordereddict.keys():
    print(i, ordereddict[i])

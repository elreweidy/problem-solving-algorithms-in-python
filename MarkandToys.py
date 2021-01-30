#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maximumToys function below.
def maximumToys(prices, k):
    maxn = 0
    spent = 0
    for i in sorted(prices):
        spent += i
        if spent < k:
            maxn += 1
    return maxn


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()

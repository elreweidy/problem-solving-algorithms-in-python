#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0
    first = 0
    last = 0
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    first = a[0]
    last = a[-1]
    print("Array is sorted in %d swaps" % (swaps) + ".")
    print("First Element: %d" % (first))
    print("Last Element: %d" % (last))


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

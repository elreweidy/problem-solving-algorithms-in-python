#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    gt = 0
    for i in range(n):
        if arr[i] + d in arr and arr[i] + 2 * d in arr:
            gt += 1
    return gt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    z = 0

    for i in range(0, n):
        z = z + 1
        if arr[i] > 0:
            positive = positive + 1


        elif arr[i] < 0:
            negative = negative + 1

        else:
            zero = zero + 1
    print(positive / z, "\n", negative / z, "\n", zero / z)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

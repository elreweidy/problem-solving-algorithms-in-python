#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    max = scores[0]
    min = scores[0]
    maxNumber = 0
    minNumber = 0
    for i in scores:

        if i > max:
            max = i
            maxNumber += 1


        elif i < min:

            min = i

            minNumber += 1

    return maxNumber, minNumber


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

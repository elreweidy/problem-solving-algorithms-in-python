#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    ups = 0
    downs = 0
    vallies = 0
    seal = False
    if path[0] == 'U':
        ups += 1
        for i in range(1, steps):
            if path[i] == 'U':
                ups += 1

            elif path[i] == 'D':
                downs += 1
                if ups == downs:
                    seal = True

    if seal == True or path[0] == 'D':
        ups = 0
        downs = 0

        for i in range(steps):
            if path[i] == 'D':
                downs += 1

            elif path[i] == 'U':
                ups += 1
                if ups == downs:
                    vallies += 1
        return vallies
    else:
        return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

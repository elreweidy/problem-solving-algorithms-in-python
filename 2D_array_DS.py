#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglasses = []
    hour_sum = 0
    rotation = 6
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            hour_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][
                j + 1] + arr[i + 2][j + 2]
            hourglasses.append(hour_sum)

    return max(hourglasses)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

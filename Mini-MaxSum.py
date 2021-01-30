#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum = 0
    x = 0
    z = 0
    for i in arr:
        sum += i
    if (sum - arr[0] > sum - arr[1] and sum - arr[0] > sum - arr[2] and sum - arr[0] > sum - arr[3] and sum - arr[
        0] > sum - arr[4]):
        x = sum - arr[0]
    elif (sum - arr[1] > sum - arr[0] and sum - arr[1] > sum - arr[2] and sum - arr[1] > sum - arr[3] and sum - arr[
        1] > sum - arr[4]):
        x = sum - arr[1]
    elif (sum - arr[2] > sum - arr[0] and sum - arr[2] > sum - arr[1] and sum - arr[2] > sum - arr[3] and sum - arr[
        2] > sum - arr[4]):
        x = sum - arr[2]
    elif (sum - arr[3] > sum - arr[0] and sum - arr[3] > sum - arr[1] and sum - arr[3] > sum - arr[2] and sum - arr[
        3] > sum - arr[4]):
        x = sum - arr[3]

    else:
        x = sum - arr[4]

    if (sum - arr[0] < sum - arr[1] and sum - arr[0] < sum - arr[2] and sum - arr[0] < sum - arr[3] and sum - arr[
        0] < sum - arr[4]):
        z = sum - arr[0]
    elif (sum - arr[1] < sum - arr[0] and sum - arr[1] < sum - arr[2] and sum - arr[1] < sum - arr[3] and sum - arr[
        1] < sum - arr[4]):
        z = sum - arr[1]
    elif (sum - arr[2] < sum - arr[0] and sum - arr[2] < sum - arr[1] and sum - arr[2] < sum - arr[3] and sum - arr[
        2] < sum - arr[4]):
        z = sum - arr[2]
    elif (sum - arr[3] < sum - arr[0] and sum - arr[3] < sum - arr[1] and sum - arr[3] < sum - arr[2] and sum - arr[
        3] < sum - arr[4]):
        z = sum - arr[3]

    else:
        z = sum - arr[4]

    print(z, x)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

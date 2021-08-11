#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#

def whatFlavors(cost, money):
    flavors_dict = {}

    for i, c in enumerate(cost):
        if c in flavors_dict:
            print(flavors_dict[c], i + 1)
            break
        else:
            flavors_dict[money - c] = i + 1


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)

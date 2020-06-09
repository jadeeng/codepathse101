#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'last_factorial_digit' function below that
# computes the factorial of n and returns the last digit
# of the factorial n.
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def last_factorial_digit(n):
    i=1
    factorial=1
    lastNumber=0
    while i<=n:
        factorial=factorial*i
        i=i+1
    lastNumber=factorial%10
    return (lastNumber)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = last_factorial_digit(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'FizzBuzz' function below.
#
# This function takes in integer n as a parameter
# and prints out its value, fizz if n is divisible
# by 3, buzz if n divisible by 5, and fizzbuzz 
# if n is divisible by 3 and 5. 
#

def FizzBuzz(n):
    i=1
    while (n>=i):
        if (i%3==0 and i%5==0):
            print("fizzbuzz")
        elif(i%3==0):
            print("fizz")
        elif(i%5==0):
            print("buzz")
        else:
            print(i)
        i=i+1


if __name__ == '__main__':
    n = int(input().strip())

    FizzBuzz(n)


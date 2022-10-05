#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n=len(arr)
    negco=0
    poco=0
    zer=0
    for i in arr:
        if(i<0):
            negco+=1
        elif(i>0):
            poco+=1
        else:
            zer+=1
    negpro=negco/n
    popro=poco/n
    zepro=zer/n
    print(popro)
    print(negpro)
    print(zepro)
       
    
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

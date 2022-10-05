#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    n=len(arr)
    arr.sort()
    ma=arr[n-1]
    mi=arr[0]
    masum=0
    misum=0
     
    if(ma==mi):
        masum=4*ma
        misum=masum
    else:
        for i in range(0,len(arr)):
            if(arr[i]!=mi):
                masum+=arr[i]
            misum=(masum-ma)+mi
   
    print(misum,masum,sep=" ")
    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

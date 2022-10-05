#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    n=len(s)
    
    std=s.split(":")
    hour=std[0]
    mi=std[1]
    sec=s[(n-4):(n-2)]
    out=""
    if(s[(n-2):n]=="PM" and hour!="12"):
        temp=int(hour)
        temp+=12
        print(temp,mi,sec,sep=":",end="")
    elif(s[(n-2):n]=="AM" and hour=="12"):
        hour="00"
        print(hour,mi,sec,sep=":",end="")
    elif(s[(n-2):n]=="PM" and hour=="12"):
        print(hour,mi,sec,sep=":",end="")
    else:
        print(hour,mi,sec,sep=":",end="")
        
        
    
    
    

    
    
    
    # Write your code here

if __name__ == '__main__':
   

    s = input()

    timeConversion(s)
   

    

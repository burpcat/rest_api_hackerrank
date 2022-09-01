#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getNumDraws' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER year as parameter.
#
import requests


def getNumDraws(year):
    
    count=0
    
    #team1goals = 13 doesnt return any data
    for i in range(12): 
        subresp = requests.get(f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1goals={i}&team2goals={i}')
        subrespjson = subresp.json()
        
        #API only prints matches which have ties
        count+= subrespjson['total']
    
    return count
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = getNumDraws(year)

    fptr.write(str(result) + '\n')

    fptr.close()


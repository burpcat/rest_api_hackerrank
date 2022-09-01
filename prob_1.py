#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#

import requests
# {'page': 1, 'per_page': 10, 'total': 6, 'total_pages': 1,
response = requests.get('https://jsonmock.hackerrank.com/api/football_matches?year=2011&team1=Barcelona&page=1')

#print(response.json())

def getTotalGoals(team, year):
    sample = requests.get(f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page=1')
    
    sampleresp = sample.json()
    
    team1goals = 0
    team2goals = 0
    
    for page in range(1,sampleresp['total_pages']+1):
        team1 = requests.get(f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={page}')
        team1resp = team1.json()
        for i in range(len(team1resp['data'])):
            team1goals += int(team1resp['data'][i]['team1goals'])
            
            
    for page in range(1,sampleresp['total_pages']+1):
        team2 = requests.get(f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={page}')
        team2resp = team2.json()
        for i in range(len(team2resp['data'])):
            team2goals += int(team2resp['data'][i]['team2goals'])
        
            
    
    return team1goals+team2goals
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    team = input()

    year = int(input().strip())

    result = getTotalGoals(team, year)

    fptr.write(str(result) + '\n')

    fptr.close()


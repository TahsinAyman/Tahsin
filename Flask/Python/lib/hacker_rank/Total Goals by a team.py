#!/bin/python3

import math
import os
import random
import re
import sys
import requests
import json


#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#

def getTotalGoals(team, year):
    cnt = 0
    team1_sum = 0
    while True:
        cnt += 1
        responce = requests.get(
            f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={cnt}")
        data = json.loads(responce.text)
        if not data['data']:
            break
        for i in data['data']:
            team1_sum += int(i['team1goals'])
    cnt = 0
    team2_sum = 0
    while True:
        cnt += 1
        responce = requests.get(f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={cnt}")
        data = json.loads(responce.text)
        if not data['data']:
            break
        for i in data['data']:
            team2_sum += int(i['team2goals'])
    return team1_sum + team2_sum


if __name__ == '__main__':
    print(getTotalGoals(input(), int(input().strip())))
    # 47
    # 23

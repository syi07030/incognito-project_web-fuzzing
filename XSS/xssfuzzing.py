# python3 XSSFuzzing.py -u https://127.0.0.1

import sys
import argparse

from requester import requester
from config import fuzzes, converter, headers
"""
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='url', dest='target')
args = parser.parse_args()

target = args.target
"""

target = input("url을 입력하세요 : ")
paramData, target = converter(target)

if not target.startswith('http'):
    try:
        response = requester('https://' + target, headers, paramData)
        target = 'https://' + target
    except:
        target = 'http://' + target

if requester(target, headers, paramData) == -1:
    sys.exit(-1)

print()
print('======= Starting Fuzzing =======')

for fuzz in fuzzes:
    print()
    paramData[list(paramData.keys())[0]] = fuzz
    try:
        requester(target, headers, paramData)
        print('[Pass] : '+fuzz)
    except:
        print('[Error] : '+fuzz)

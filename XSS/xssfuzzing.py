# python xssfuzzing.py -u https://url.com

import sys

from requester import requester
from config import fuzzes, converter, headers

"""URL option
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='url', dest='target')
args = parser.parse_args()
target = args.target
"""

target = sys.argv[1]

paramData, target = converter(target)

if requester(target, headers, paramData) == -1:
    sys.exit(-1)

print('\n======= Starting Fuzzing =======\n')

for fuzz in fuzzes:
    paramData[list(paramData.keys())[0]] = fuzz
    try:
        requester(target, headers, paramData)
        print('[Pass] : '+fuzz+'\n')
    except:
        print('[Error] : '+fuzz+'\n')

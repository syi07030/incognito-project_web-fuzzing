# python xssfuzzing.py https://url.com

import sys

from requester import requester
from config import fuzzes, headers
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse, quote

"""URL option
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='url', dest='target')
args = parser.parse_args()
target = args.target
"""

target = sys.argv[1]

#paramData, target = converter(target)

if requester(target, headers) == -1:
    sys.exit(-1)

print('\n======= Starting Fuzzing =======\n')

for fuzz in fuzzes:
    parts = urlparse(target)
    qsl = dict(parse_qsl(parts.query))
    if bool(qsl):
        qsl[list(qsl.keys())[0]] = fuzz
        parts = parts._replace(query=urlencode(qsl))
        new_target = urlunparse(parts)
    else:
        new_target = target+'?'+quote(fuzz)
    try:
        requester(new_target, headers)
    except:
        print('[Error] : '+new_target+'\n')

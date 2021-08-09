import directory_fuzzer
import sqli
import xssfuzzing

if __name__ == "__main__":
    print("=============start============")
    url = input("target url: ")
#    paramData, url = converter(url)
#    if not url.startswith('http'):
#        try:
#            response = requester('https://' + url, headers, paramData)
#            url = 'https://' + url
#        except:
#            url = 'http://' + url
#
#    if requester(url, headers, paramData) == -1:
#        sys.exit(-1)

    print(">>>sql injection<<<")
    if __name__ == "__main__":
    if url:
        result = scan_page(url if url.startswith("http") else "http://%s" % url, None)
        print("\nscan results: %s vulnerabilities found" % ("possible" if result else "no"))
    else:
        print("wrong input")

    print(">>>path traversal<<<")
    print("Random Success: ",directory_fuzzer.random_path(url))
    print("Existed Success: ", directory_fuzzer.existed_path(url))

    print(">>>xss injection<<<")
    xssfuzzing.xssfuzzing(url)

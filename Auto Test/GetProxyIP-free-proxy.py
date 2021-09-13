import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import re

chrome_driver = "C:\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path=chrome_driver, options=options)


IPPool = []
for i in range(1, 3):
    url = 'http://free-proxy.cz/zh/proxylist/country/US/https/ping/all/{}'.format(i)
    print('Dealing with {}'.format(url))
    driver.get(url)
    soup = BeautifulSoup(driver.page_source)
    for j in soup.select('tbody > tr'):
        if re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', str(j)):
            IP = re.findall(
                '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', str(j))[0]
            Port = re.findall('class="fport" style="">(.*?)</span>', str(j))[0]
            IPPool.append(pd.DataFrame([{'IP': IP, 'Port': Port}]))
    print('There are {} IPs in Pool'.format(len(IPPool)))
IPPool = pd.concat(IPPool, ignore_index=True)
IPPool

ActIps = []
for IP, Port in zip(IPPool['IP'], IPPool['Port']):
    proxy = {'http': 'http://' + IP + ':' + Port,
             'https': 'https://' + IP + ':' + Port}
    try:
        # 隨機找的一篇新聞
        url = 'https://www.chinatimes.com/realtimenews/20200205004069-260408'
        resp = requests.get(url, proxies=proxy, timeout=2)
        if str(resp.status_code) == '200':
            ActIps.append(pd.DataFrame([{'IP': IP, 'Port': Port}]))
            print('Succed: {}:{}'.format(IP, Port))
        else:
            print('Failed: {}:{}'.format(IP, Port))
    except:
        print('Failed: {}:{}'.format(IP, Port))

# ActIps = pd.concat(ActIps, ignore_index=True)
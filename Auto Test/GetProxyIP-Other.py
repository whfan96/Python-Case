import scrapy
from bs4 import BeautifulSoup
import json


'''
請參考網址步驟操作
https://ithelp.ithome.com.tw/articles/10208575

scrapy startproject get_proxy
cd get_proxy
scrapy genspider proxy_example www.us-proxy.org

'''

class ProxyExampleSpider(scrapy.Spider):
    name = 'proxy_example'
    allowed_domains = ['www.xicidaili.com']
    start_urls = ['http://www.xicidaili.com/nn/%s' % i for i in range(1, 6)]

    def parse(self, response):
        # position()>1 獲取tr標籤位置大於1的標籤
        for sel in response.css('table#ip_list').xpath('.//tr[position()>1]'):
            # nth-child(2)獲取第二個子標籤 （注意這裡的順序從1開始）
            ip = sel.css('td:nth-child(2)::text').extract_first()  # ip
            port = sel.css('td:nth-child(3)::text').extract_first()  # 埠
            # 型別HTTP，https
            scheme = sel.css('td:nth-child(6)::text').extract_first()

            # 拼接代理url
            proxy = '%s://%s:%s' % (scheme, ip, port)

            # 定義json資料 meta 文字
            meta = {
                'proxy': proxy,
                'dont_retry': True,  # 只下載一次，失敗不重複下載
                'download_timeout': 10,    # 設定等待時間

                '_proxy_ip': ip,
                '_proxy_scheme': scheme
            }

            # 校驗代理是否可用  通過訪問httpbin.org/ip,進行檢測
            url = '%s://httpbin.org/ip' % scheme
            yield scrapy.Request(url, callback=self.check, meta=meta, dont_filter=True)

    def check(self, response):
        proxy_ip = response.meta['_proxy_ip']
        proxy_scheme = response.meta['_proxy_scheme']

        # json.loads（）將json文字返回字典型別   origin原代理
        if json.loads(response.text)['origin'] == proxy_ip:
            yield {
                'proxy': response.meta['proxy'],
                'scheme': proxy_scheme,
            }

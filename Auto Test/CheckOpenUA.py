from selenium import webdriver
from fake_useragent import UserAgent
import time

# user-agent
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"

# driver
chrome_driver = "C:\chromedriver.exe"

# 關閉通知提醒
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# https://stackoverflow.com/questions/53039551/selenium-webdriver-modifying-navigator-webdriver-flag-to-prevent-selenium-detec
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# 使用無痕模式。用 selenium 開瀏覽器已經很乾淨了，但疑心病重的可以用一下
chrome_options.add_argument("--incognito")


'''
fake_useragent請參考：https://ithelp.ithome.com.tw/articles/10224979
'''
ua = UserAgent()
user_agent = ua.random
chrome_options.add_argument(
    "user-agent={}".format(user_agent))  # 使用偽造的 user-agent

# chrome_options.add_argument('--proxy-server=http://219.239.142.253:3128')  # 讓 selenium透過 tor訪問 internet,可以參考 https://hardliver.blogspot.com/2018/04/selenium.html

driver = webdriver.Chrome(executable_path=chrome_driver,
                          chrome_options=chrome_options)  # 使用 selenium開啟瀏覽器

# 訪問 statcounter來確認目前瀏覽器的 user-agent
driver.get('http://gs.statcounter.com/detect')
time.sleep(10)

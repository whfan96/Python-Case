import os
from selenium import webdriver  # 還沒安裝就先 pip install selenium

userId = ""
password = ""

# chromedriver路徑
chrome_driver = "C:\chromedriver.exe"

# 選定使用chromedriver
driver = webdriver.Chrome(chrome_driver)
driver.implicitly_wait(10)  # 等待頁面好 10秒內

# 打開瀏覽器
url = "https://www.instagram.com/"  # 目標網址 ig官網

# 打開網址
driver.get(url)

# 取得帳號位置
user_input = driver.find_element_by_xpath(
    '//*[@id="loginForm"]/div/div[1]/div/label/input')
user_input.clear()  # 清除原本裡面的東西確保乾淨
user_input.send_keys(userId)  # 帳號

# 取得密碼位置
user_input = driver.find_element_by_xpath(
    '//*[@id="loginForm"]/div/div[2]/div/label/input')
user_input.clear()
user_input.send_keys(password)  # 密碼

# 找到登入按鈕位置
login_button = driver.find_element_by_xpath(
    '//*[@id="loginForm"]/div[1]/div[3]/button')
login_button.click()  # 點一下

# 切換網頁
url = "https://www.instagram.com/p/BySVEmQH2hl/"  # 方容國的貼文
driver.get(url)

# 找到按讚的按鈕
best_button = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button')
t = best_button.find_element_by_class_name("_8-yf5")  # 選到文字讚的那個class
t = t.get_attribute("aria-label")  # 取出文字

# 檢驗是讚還是收回按 是讚就按下去
if t == '讚':
    best_button.click()  # 點讚

# 關閉瀏覽器
driver.close()
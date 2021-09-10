# 抓取 Medium.com 原始碼的網頁
import urllib.request as req
import json

url = "https://medium.com/_/api/home-feed"

# 加入底下這一段才會讓整段程式碼看起來像一個普通使用者，建立一個Request物件，付加Request Headers 的資訊
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
})

# 使用 with request.urlopen(網址) 連上網路，並將其重新取名為 response ，最後使用 read() 函數，將網頁結果放入 data 中。
# 原本 req.urlopen 的括號內會放網址而已，但為了讓我們更像一般使用者，這邊放入剛剛建立的物件request。
with req.urlopen(request) as response:
    # 取的網頁的原始碼。並用decode("utf-8")來翻譯成中文（解碼），在此範例中，根據觀察網頁原始碼，抓到的資料格式是json格式
    data = response.read().decode("utf-8")

# 解析 JSON 格式的資料，取得文章標題 （json格式是大括號跟中括號，大括號代表字典、中括號代表列表）
# 這組字串是網頁原始碼的字串，根據觀察，這一段程式碼會阻礙json格式解析(因為這段字串不是json格式)，所以將這段字串改為空字串後再執行程式
data = data.replace("])}while(1);</x>", "")
# 把原始資料解析成字典/列表的資料表現型式，讀取檔案內資料時是load()，將資料轉換成字典/列表用loads()
data = json.loads(data)
# print(data)
# 取得json資料中的文章標題
posts = data["payload"]["references"]["Post"]
for key in posts:
    post = posts[key]
    print(post["title"])

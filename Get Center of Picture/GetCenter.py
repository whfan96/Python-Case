from PIL import Image

def Find_Origin(picture):
    # img = ImageGrab.grab()    # 抓取當前螢幕的快照，返回一個 RGB 影象
    # img.save(picture)    # 儲存圖片
    img = Image.open(picture)
    (w, h) = img.size
    x = w/2
    y = h/2
    return str(x) + "," + str(y)

imageFile = input("請輸入圖片完整路徑：")
s = str(Find_Origin(imageFile))
s = s.split(',')
print("圖片中心點：x = %s, y = %s" % (s[0], s[1]))

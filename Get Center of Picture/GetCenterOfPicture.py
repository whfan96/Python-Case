from PIL import Image
from PIL import ImageGrab

color = [46, 49, 57]


def Find_Coordinate(picture, color):    # 找邊界四點座標
    img = Image.open(picture)
    img_load = img.load()
    img_x = []
    img_y = []
    width, height = img.size
    for i in range(0, width):
        for j in range(0, height):
            if img_load[i, j][0] == color[0] and img_load[i, j][1] == color[1] and img_load[i, j][2] == color[2]:
                img_x.append(i)
                img_y.append(j)
    return [max(img_x), min(img_x), max(img_y), min(img_y)]


def Find_Origin(picture):
    # img = ImageGrab.grab()    # 抓取當前螢幕的快照，返回一個 RGB 影象
    # img.save(picture)    # 儲存圖片
    coordinate = Find_Coordinate(picture, color)
    x = ((coordinate[0]-coordinate[1])//2)+coordinate[1]
    y = ((coordinate[2]-coordinate[3])//2)+coordinate[3]
    return str(x) + "," + str(y)


imageFile = input("請輸入圖片完整路徑：")
s = Find_Origin(imageFile)
print("圖片中心點：" + str(s))

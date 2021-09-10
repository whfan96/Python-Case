from PIL import Image
from GetCenterOfPicture import Find_Coordinate

color = [46, 49, 57]


def Cropped_Image(picture, save_path):
    side = Find_Coordinate(picture, color)
    img = Image.open(picture)
    img = img.crop((side[1], side[3], side[0], side[2]))
    img.save(save_path)


imageFile = input("請輸入原始圖片完整路徑：")
savePath = input("請輸入剪裁圖片儲存位置：")
saveName = input("請輸入剪裁圖片儲存名稱：")

Cropped_Image(imageFile, savePath + saveName)

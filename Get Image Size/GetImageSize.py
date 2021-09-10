from PIL import Image

imageFile = input("請輸入圖片完整路徑：")
img = Image.open(imageFile)
(w, h) = img.size
print("寬 = %d, 高 = %d" % (w, h))
# img.show()
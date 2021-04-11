import sys
from PIL import Image

imageFile = input("請輸入圖片完整路徑：")
img = Image.open(imageFile)
(w, h) = img.size
print('w=%d, h=%d' % (w, h))
# img.show()
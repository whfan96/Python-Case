import cv2
# 載入分類器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0) # 從視訊鏡頭擷取影片
# cap = cv2.VideoCapture('filename.mp4')  # 使用現有影片

while True:
    # Read the frame
    _, img = cap.read()
# 轉成灰階
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 偵測臉部
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# 繪製人臉部份的方框
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# 顯示成果
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)  # 正常視窗大小
    cv2.imshow('img', img)  # 秀出圖片
# Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break;

# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()

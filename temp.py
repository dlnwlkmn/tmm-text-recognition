import cv2
from pytesseract import pytesseract

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 1) # Частота кадров
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600) # Ширина кадров в видеопотоке.
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # Высота кадров в видеопотоке.

img = cv2.imread("text.png")

letters = pytesseract.image_to_string(img)

print(letters)

cv2.imshow("window", img)
cv2.waitKey(0)


# while True:
#     ret, img = cap.read()
#     if ret == False: # Клавиша q
#         break
#     img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
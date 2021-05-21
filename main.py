import cv2
import time
from pytesseract import pytesseract
from pytesseract import Output

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# img = cv2.imread("text.png")
#
# img_text = pytesseract.image_to_string(img)
#
# print(img_text)

# img_data = pytesseract.image_to_data(img, output_type=Output.DICT)
#
# for i, word in enumerate(img_data["text"]):
#     if word != "":
#         x, y, w, h = img_data["left"][i], img_data["top"][i], img_data["width"][i], img_data["height"][i]
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
#         cv2.putText(img, word, (x, y - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
#
# cv2.imshow("camera", img)
# cv2.waitKey(0)

face_db = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_alt.xml")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 1) # Частота кадров
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600) # Ширина кадров в видеопотоке.
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # Высота кадров в видеопотоке.

while True:
    ret, img = cap.read()
    if ret == False: # Клавиша q
        break
    # img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    img_data = pytesseract.image_to_data(img, output_type=Output.DICT)

    for i, word in enumerate(img_data["text"]):
        if word != "":
            x,y,w,h = img_data["left"][i],img_data["top"][i],img_data["width"][i],img_data["height"][i]
            cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img, word, (x,y-8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    # smiles = face_db.detectMultiScale(img_gray, 1.1, 19)

    # for (x, y, w, h) in smiles:
    #     cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("camera", img)
    if cv2.waitKey(10) & 0xff == ord('q'): # Клавиша q
        break
    time.sleep(0.3)

cap.release()
cv2.destroyAllWindows()
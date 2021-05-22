import cv2
from pytesseract import pytesseract
from pytesseract import Output

# Путь до установленной программы по распознаванию текста
pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# pytesseract.tesseract_cmd = "/usr/local/Cellar/tesseract/4.1.1/bin/tesseract.exec"

# One picture text recognition
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

# Объект видеокамеры
cap = cv2.VideoCapture(0)

# Настрока параметров вебкамеры
cap.set(cv2.CAP_PROP_FPS, 24) # Частота кадров
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480) # Ширина кадров в видеопотоке.
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320) # Высота кадров в видеопотоке.

# For face recognition
# face_db = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_alt.xml")

# Жизненный цикл программы
while True:
    # Чтение кадра камеры
    ret, img = cap.read()
    # условие выхода, в случае отсутсвия картинки с камеры
    if ret == False:
        break

    img_data = pytesseract.image_to_data(img, output_type=Output.DICT)

    # Вывод обводки для распознанных слов на кадре,
    # и самих слов над распознанными
    for i, word in enumerate(img_data["text"]):
        if word != "":
            x,y,w,h = img_data["left"][i],img_data["top"][i],img_data["width"][i],img_data["height"][i]
            cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img, word, (x,y-8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    # For face recognition
    # img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # smiles = face_db.detectMultiScale(img_gray, 1.1, 19)
    #
    # for (x, y, w, h) in smiles:
    #     cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
    # cv2.imshow("camera", img)

    # Вывод кадра в окно
    cv2.imshow("camera", img)
    # Условие выхода из цикла (кнопка q)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break

# Уничтожаем объект камеры и окна
cap.release()
cv2.destroyAllWindows()
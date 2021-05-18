import cv2

face_db = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_alt.xml")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 1) # Частота кадров
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600) # Ширина кадров в видеопотоке.
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # Высота кадров в видеопотоке.

while True:
    ret, img = cap.read()
    if ret == False: # Клавиша q
        break
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    smiles = face_db.detectMultiScale(img_gray, 1.1, 19)

    for (x, y, w, h) in smiles:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("camera", img)
    if cv2.waitKey(10) & 0xff == ord('q'): # Клавиша q
        break

cap.release()
cv2.destroyAllWindows()
import numpy as np
import cv2
eye_classifier = cv2.CascadeClassifier(r'C:\Users\User\Downloads\Harcascade\haarcascade_eye.xml')
face_classifier= cv2.CascadeClassifier(r'C:\Users\User\Downloads\Harcascade\haarcascade_frontalface_default.xml')
img= cv2.imread(r'C:\Users\User\Downloads\Harcascade\pic.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

eyes = eye_classifier.detectMultiScale(gray, 1.2, 4)
faces = face_classifier.detectMultiScale(gray, 1.3, 5)

# When no faces detected, face_classifier returns and empty tuple
if faces.size == 0:

    print("No Face Found")

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (127, 0, 255), 2)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]

    eyes = eye_classifier.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 255, 0), 2)
        cv2.imshow('img', img)
        cv2.waitKey(0)

cv2.destroyAllWindows()

# FACE DETECTION IN PHOTO

import cv2

cap=cv2.VideoCapture(0)
ret,photo=cap.read()

#use this  line no 9 when you want to detect faces in a photo and comment above two lines
#photo=cv2.imread('multiplep.jpg')
model=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
x=model.detectMultiScale(photo)
if not(len(x)==0):
    for(i,j,k,l) in x:
        
        nphoto=cv2.rectangle(photo,(i,j),(i+k,j+l),(255,0,255),5)
        cv2.imshow("myphoto",nphoto)
        cv2.imwrite("det.jpg",nphoto)
        cv2.waitKey()==13
    cv2.destroyAllWindows()
else:
    print(" This place is so dark,that we cannot detect your face")
cap.release()

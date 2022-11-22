# FACE DETECTION IN LIVE CAPTURED VIDEO
import cv2
cap=cv2.VideoCapture(0)
#ret,photo=cap.read()
#to save the video the first we are checking requirements
photo=cv2.imread('muiltiplep.jpg')
if(cap.isOpened)==False:
    print("Error while reading the file")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('myvideo.avi', fourcc, 20.0, (640, 480)) 

model=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    ret,photo=cap.read()
    x=model.detectMultiScale(photo)
    if not(len(x)==0):
        
        for(i,j,k,l) in x:
        
            nphoto=cv2.rectangle(photo,(i,j),(i+k,j+l),(255,0,255),5)
        out.write(nphoto)
        cv2.imshow("myphoto",nphoto)
        n=cv2.waitKey(10)
        if n==13:
            cv2.destroyAllWindows()
            break
          
    else:
        print(" May be this place is so  dark or may be there is no face  to detect")

cap.release()

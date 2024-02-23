import cv2
import numpy as np 
cap = cv2.VideoCapture(0)
#rescale saja default 75% dari 640x320
def rescale_frame(frame,percent=75):
    width=int(frame.shape[1]*percent/100)
    height=int(frame.shape[0]*percent/100)
    dim = (width,height)
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)
#MENAMPILKAN VIDEO
while(cap.isOpened()):
    ret, frame = cap.read()
    image=rescale_frame(frame,percent=100)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    edge=cv2.Canny(gray,40,250)
    contours, hierarchy = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    jumlah=str(len(contours))
    print("jumlah objek : ",jumlah)
    
    result_contour=cv2.drawContours(image,contours,-1,(0,255,0),2)
    cv2.imshow("rsult_contour",result_contour)
    #cv2.imshow("Kamera",gray)
    cv2.imshow("Edge,",edge)
    #interrupt=cv2.waitkey(10)
    #cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()





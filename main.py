import cv2
import numpy
from pyzbar.pyzbar import decode



cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    
    for info in decode(img):
        myData = info.data.decode('utf-8')
        print(myData)

    cv2.imshow("Result", img) 
       
cv2.destroyAllWindows()
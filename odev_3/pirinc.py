import cv2
import numpy as np 
import matplotlib.pyplot as plt


foto = cv2.imread("image2.jpg",flags=0)
foto= cv2.resize(foto, (600,800))

ret,  thresh1 = cv2.threshold(foto, 100, 255, cv2.THRESH_BINARY) # eşiklenmiş foto


canny = cv2.Canny(thresh1, 0, 255)  #siyah beyaz değerlere göre değişimin net başladığı yere göre dış hatlarını belirtir

(cnt, hierarchy) = cv2.findContours( 
    canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
rgb = cv2.cvtColor(thresh1, cv2.COLOR_BGR2RGB) 
cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2) 

print(len(cnt))
cv2.imshow("origifoto",foto)
cv2.imshow("binaryimage",thresh1)
cv2.imshow("s",rgb) 

cv2.waitKey()


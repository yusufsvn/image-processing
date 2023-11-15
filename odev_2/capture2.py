import cv2
import numpy as np
vid =cv2.VideoCapture(0)

while True:
    a,kare = vid.read()  
    
    kare=cv2.cvtColor(kare, cv2.COLOR_BGR2HSV)
    

    alt_sinir= np.array([0, 100, 20])
    ust_sinir = np.array([10, 255, 255])

    maske=cv2.inRange(kare, alt_sinir, ust_sinir)
    
    kare_rgb=cv2.cvtColor(kare, cv2.COLOR_HSV2BGR)
    sadece_kirmizi = cv2.bitwise_and(kare,kare, mask= maske)
    cv2.imshow("kare",kare_rgb)
    cv2.imshow("maske",maske)
    cv2.imshow("only_red",sadece_kirmizi)
   
    if cv2.waitKey(1) == ord('q'):
        break
    
    
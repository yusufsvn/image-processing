import cv2
foto = cv2.imread("mordekai.jpeg",flags=0)
#cv2.imshow("wa",foto)
#cv2.waitKey()

hist = []
for a in range(256): #bu dongu 256 tane değeri indexlerde tutmak icin butun elemanlara 0 atar
    hist.append(0)
#print(hist) 

for i in range(len(foto)): # sutun    matris icinde gezinen dongu
    for j in range(len(foto[0])):  #satir     
        sayitutucu = foto[i][j]    #gezdigi matristeki degerleri bulur sayitutucu degişkenine atar
        hist[sayitutucu]+=1        #buldugu degere gore hist listesinde index tutar ve 1 arttırır 
                                

print(hist)
import cv2 as cv

video = cv.VideoCapture(0)

while True:
    ret,img = video.read()


    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    gray = cv.medianBlur(gray, 5)
    
    edges = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9,9)
    
    color = cv.bilateralFilter(img, 9,300,300)
    
    cartoon = cv.bitwise_and(color,color, mask=edges)
    
    cv.imshow("cartoon",cartoon)
    cv.imshow('original',img)
    k = cv.waitKey(1)
    if k==ord('q'):
        break
video.release()
cv.destroyallwindows()


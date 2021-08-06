import cv2 as cv
import numpy as np

def empty(img):
	pass

cap = cv.VideoCapture(0)

cv.namedWindow("Trackbar")
cv.resizeWindow("Trackbar",600,300)
cv.createTrackbar("hue_min","Trackbar",0,179,empty)
cv.createTrackbar("hue_max","Trackbar",179,179,empty)
cv.createTrackbar("sat_min","Trackbar",0,255,empty)
cv.createTrackbar("sat_max","Trackbar",255,255,empty)
cv.createTrackbar("val_min","Trackbar",0,255,empty)
cv.createTrackbar("val_max","Trackbar",255,255,empty)


while True:
	ret,frame = cap.read()

	hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
	hue_min = cv.getTrackbarPos("hue_min","Trackbar")
	hue_max = cv.getTrackbarPos("hue_max","Trackbar")
	sat_min = cv.getTrackbarPos("sat_min","Trackbar")
	sat_max = cv.getTrackbarPos("sat_max","Trackbar")
	val_min = cv.getTrackbarPos("val_min","Trackbar")
	val_max = cv.getTrackbarPos("val_max","Trackbar")

	lower = np.array([hue_min, sat_min, val_min])
	upper = np.array([hue_max, sat_max, val_max])

	mask = cv.inRange(hsv,lower,upper)

	cnts,hei = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
	for c in cnts:
		area = cv.contourArea(c)
		if area > 300:
			peri = cv.arcLength(c,True)
			approx = cv.approxPolyDP(c,0.02*peri, True)
			x,y,w,h = cv.boundingRect(c)
			cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
		if len(approx) == 4:
			cv.putText(frame,"Rectangle: ", (x+w+20, y+h+20), cv.FONT_HERSHEY_COMPLEX, 0.7 ,(0,0,255),2)
		elif len(approx) == 3:
			cv.putText(frame,"Triangle: ", (x+w+20, y+h+20), cv.FONT_HERSHEY_COMPLEX, 0.7 ,(77,22,255),2)
		else:
			cv.putText(frame,"Circle:", (x+w+20, y+h+20), cv.FONT_HERSHEY_COMPLEX, 0.7 ,(0,66,255),2)
		print(len(approx))
	cv.imshow("frames",frame)
	cv.imshow("hsv",hsv)
	cv.imshow('Mask',mask)

	k=cv.waitKey(1)
	if k==ord('q'):
		break
cap.release()
cv.destroyAllWindows()
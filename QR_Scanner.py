import cv2 as cv
import pyzbar.pyzbar as pyzbar   # decode QR code

cap = cv.VideoCapture(0)

while True:
	ret,frame = cap.read()
	detect = pyzbar.decode(frame)
	for obj in detect:
		cv.rectangle(frame,(720,0), (00, 70),(50,50,32),-2)
		cv.putText(frame, str(obj.data), (40,50), cv.FONT_HERSHEY_SIMPLEX, 2, (255,0,43), 3)


	cv.imshow("frames",frame)

	k=cv.waitKey(1)
	if k==ord('q'):
		break
cap.release()
cv.destroyAllWindows()
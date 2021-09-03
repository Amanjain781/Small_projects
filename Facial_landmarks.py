import cv2 as cv
import numpy as np
import dlib
import datetime


cap = cv.VideoCapture(0,cv.CAP_DSHOW)
detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


fps_start_time = datetime.datetime.now()
fps = 0
total_frames = 0

while True:
    _,frame =cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    total_frames +=1
    #print(total_frames)
    
    faces = detector(gray)
    
    for face in faces:
        face_landmarks = predictor(gray, face)
        
        for n in range(0,68):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            cv.circle(frame, (x,y), 1, (0,0,255), 1)
            
    
    fps_end_time = datetime.datetime.now()
    time_diff = fps_end_time - fps_start_time
    
    if time_diff.seconds == 0:
        fps= 0.0
    else:
        fps = (total_frames/ time_diff.seconds )
    print(time_diff.seconds )
    
    fps_text = "FPS:{: .2f}".format(fps)
    
    
    font = cv.FONT_HERSHEY_SIMPLEX
    
    frame = cv.putText(frame, fps_text, (20, 50), font, 1, (100, 255, 255), 1, cv.LINE_AA)
    cv.imshow("Facial Landmarks",frame)   
    
    key = cv.waitKey(1) & 0xFF 
    if key == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()







        
        



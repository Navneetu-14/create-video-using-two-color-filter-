import cv2
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("video.mkv")

while True:
    ref,frame =cap.read() #read image 
    #cv2.imshow("Frame",frame) # display frame/image
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("video",frame)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)

    key = cv2.waitKey(1) #wait till key press
    if key == ord("q"):   #exit loop on 'q' key press
        break

cap.release()  #release Video capture object
cv2.destroyAllWindows() #destroy all from windows
    

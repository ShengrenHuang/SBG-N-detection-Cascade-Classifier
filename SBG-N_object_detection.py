import cv2


sbg_cascade = cv2.CascadeClassifier('cascade.xml')
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = sbg_cascade.detectMultiScale(gray, 1.1, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)


    cv2.imshow('img',frame)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break

cap.release()


cv2.destroyALLWindows()
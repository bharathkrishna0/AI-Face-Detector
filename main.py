import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade__frontalface_default.xml')
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('error')
    exit()

while True:
    ret,frame = cap.read()
    if not ret:
        print('error not retrieve frame')
        continue
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(300,300))
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('Face Detection',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
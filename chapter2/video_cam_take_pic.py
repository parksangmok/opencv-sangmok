import cv2
from cv2 import VideoCapture

cap = VideoCapture(0)
if cap.isOpened():
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('camera', frame)
            if cv2.waitKey(1) != -1:
                cv2.imwrite('photo.jpg', frame)
                break
        
        else:
            print('no frame!')
else:
    print('no frame!')
cap.release()
cv2.destroyAllWindows
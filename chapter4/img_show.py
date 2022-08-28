import cv2
import numpy as np
img = cv2.imread('C:/Users/sangmok/Documents/opencv-sangmok/img/sunset.jpg')

x = 320; y = 150; w= 50; h=40
roi = img[y:y+h, x:x+w]                #roi 지정 1

print(roi.shape)
cv2.rectangle(roi, (0,0), (h-1, w-1), (0, 255, 0))  #roi에 사각형 그리기 2
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows
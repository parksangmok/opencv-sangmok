import cv2
import numpy as np

img = cv2.imread('C:/Users/sangmok/Documents/opencv-sangmok/img/sunset.jpg')

x = 320; y = 150; w = 50; h = 50
roi = img[y:y+h, x:x+w]
img2 = roi.copy()                    #roi 배열 복제 -- 1

img[y:y+h, x+w:x+w+w] = roi          # 새로운 좌표에 roi추가, 태양 2개 만들기
cv2.rectangle(img, (x, y), (x+w+w, y+h), (0, 255, 0))  # 2개의 태양 영역에 사각형 표시

cv2.imshow('img', img)                      # 원본 이미지 출력
cv2.imshow('roi', img2)                     # roi만 따로 입력

cv2.waitKey(0)
cv2.destroyAllWindows()
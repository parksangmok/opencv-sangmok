import cv2

img_file = 'C:/Users/sangmok/Documents/opencv-sangmok/img/girl.jpg'  
img = cv2.imread(img_file)  #파일로부터 이미지 읽기

if img is not None:
    cv2.imshow('IMG', img)
    cv2.waitKey()
    cv2.destroyAllWindwos()
else:
    print('No image file')
    
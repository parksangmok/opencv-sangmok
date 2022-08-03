import cv2
img_file = "../img/girl.jpg"
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

if img is not None:
    cv2.imshow('ING', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('No image file.')
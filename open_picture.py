import cv2

file_path = "lockscreen.jpg"
img = cv2.imread(file_path)

cv2.imshow('Test', img)
cv2.resizeWindow('Test', 1080, 1080)

cv2.waitKey(0)
cv2.destroyAllWindows()


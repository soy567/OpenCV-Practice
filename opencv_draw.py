import numpy as np
import cv2

# Color 설정
blue_color = (255, 0 , 0)
green_color = (0, 255, 0)
red_color = (255, 0, 0)
white_color = (255, 255, 255)

# 점 좌표 설정
points1 = np.array([[10, 10], [170, 10], [200,230], [70, 70], [50, 150]], np.int32)
points2 = np.array([[110, 110], [270, 110], [300, 330], [170, 170], [150, 250]], np.int32)

print("Points1: " + str(points1))
print("Points2: " + str(points2))

# 모두 0으로 되어있는 빈 Canvas(검정색)
img = np.zeros((384, 384, 3), np.uint8)

# 그리기
img = cv2.polylines(img, [points1], False, blue_color, 2) # 열린 도형
img = cv2.polylines(img, [points2], True, green_color, 2) # 닫힌 도형

cv2.imshow('polylines', img)
cv2.waitKey()
cv2.destroyAllWindows()
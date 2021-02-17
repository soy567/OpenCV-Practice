import cv2 as cv
import numpy as np
import sys
import matplotlib.pyplot as plt

vid_path = "/home/soy567/Desktop/Lane_clips/영종대교 휴게소 - 인천공항고속도로 - 을왕리 해수욕장 드라이브 Night Drive_720p.mp4"
cap = cv.VideoCapture(vid_path)

if not cap.isOpened():
    print("비디오 파일 로드실패!")
    sys.exit()

while True:
    ret, frame = cap.read()

    if ret is None:
        break

    cv.imshow('Video', frame)

    if cv.waitKey(10) == 27:
        break
 
cap.release()
cv.destroyAllWindows()
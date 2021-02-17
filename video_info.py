import cv2

def video_info(infilename):
 
    cap = cv2.VideoCapture(infilename)
 
    if not cap.isOpened():
        print("could not open :", infilename)
        exit(0)
 
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
 
    print('length : ', length)
    print('width : ', width)
    print('height : ', height)
    print('fps : ', fps)

if __name__ == "__main__":
    path = "/home/soy567/Desktop/lane_mov/Day_dd.mp4"
    video_info(path)

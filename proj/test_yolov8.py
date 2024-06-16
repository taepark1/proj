import cv2
from ultralytics import YOLO
import sys
from os import system
#from PyQt5.QtWidgets import *
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
#from PyQt5 import uic
import cv2
import argparse
from queue import Queue

#import sonmari_video as sv
# Load the YOLOv8 model
#model = YOLO('yolov8n.pt')

#model = YOLO('/home/taepark/goinfre/proj/yolov8/runs/detect/train2/weights/best.pt')
model = YOLO('C:\\git\\main\\proj\\prototype\\train\\house\\best.pt')

# 동영상 파일 사용시
#video_path = "/home/taepark/goinfre/New_sample/data/REAL/WORD/01/NIA_SL_WORD1501_REAL01_D.mp4"
#video_path = "/home/taepark/goinfre/proj/123111.mp4"
cap = cv2.VideoCapture(0)

# webcam 사용시
#cap = cv2.VideoCapture(0)
#form_class = uic.loadUiType("sonmariui.ui")[0]
#class MyWindow(QMainWindow, form_class):
#    def __init__(self):
#        super().__init__()
#        self.setupUi(self)
#-------------------------------------

#-------------------------------------
# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
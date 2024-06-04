import cv2
from ultralytics import YOLO
import sys
from os import system
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, uic, QtGui
import cv2
import argparse
from queue import Queue
import time
import random
from ultralytics.utils.plotting import Annotator  # ultralytics.yolo.utils.plotting is deprecated
#from PyQt5 import QtWidgets, uic
#from PyQt5 import QtGui
from threading import Thread, enumerate
#import sonmari_video as sv
# Load the YOLOv8 model
#model = YOLO('yolov8n.pt')

#model = YOLO('/home/taepark/goinfre/proj/yolov8/runs/detect/train2/weights/best.pt')
model = YOLO('/home/taepark/goinfre/asdf.v1i.yolov8/runs/detect/train/weights/best.pt')
#model = YOLO('yolov8n.pt')
# 동영상 파일 사용시
video_path = "/home/taepark/goinfre/New_sample/data/REAL/WORD/01/NIA_SL_WORD1501_REAL01_D.mp4"
#video_path = "/home/taepark/goinfre/proj/123111.mp4"
#cap = cv2.VideoCapture(video_path)


one = {'person':'person output', 'chairs':'chair out put'}
#핵심 이미지가 하나인 수화 동작 저장

# webcam 사용시
#cap = cv2.VideoCapture(0)
#form_class = uic.loadUiType("sonmariui.ui")[0]
#class MyWindow(QMainWindow, form_class):
#    def __init__(self):
#        super().__init__()
#        self.setupUi(self)
#-------------------------------------
def parser():
    parser = argparse.ArgumentParser(description="YOLO Object Detection")
    parser.add_argument("--input", type=str, default=0,
                        help="video source. If empty, uses webcam 0 stream")
    parser.add_argument("--out_filename", type=str, default="",
                        help="inference video name. Not saved if empty")
    parser.add_argument("--weights", default="./model/yolov4-obj_96_best.weights",
                        help="yolo weights path")
    parser.add_argument("--dont_show", action='store_true',
                        help="windown inference display. For headless systems")
    parser.add_argument("--ext_output", action='store_true',
                        help="display bbox coordinates of detected objects")
    parser.add_argument("--config_file", default="./cfg/yolov4-obj.cfg",
                        help="path to config file")
    parser.add_argument("--data_file", default="./data/obj.data",
                        help="path to data file")
    parser.add_argument("--thresh", type=float, default=.70,
                        help="remove detections with confidence below this value")
    return parser.parse_args()


form_class = uic.loadUiType("sonmariui.ui")[0]

class MyApp(QtWidgets.QDialog):
    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi("sonmariui.ui", self)  # UI 파일을 먼저 로드하여 setupUi를 호출
        
        # 이미지 파일을 로드하고 QLabel 위젯에 설정
        self.pixmap = QPixmap("1.png")
        self.pixmap = self.pixmap.scaledToWidth(100)  # 이미지 크기 조정
        self.icon.setPixmap(self.pixmap)  # 'icon' QLabel에 QPixmap 객체 설정

        args = parser()

        frame_queue = Queue()
        darknet_image_queue = Queue(maxsize=1)
        detections_queue = Queue(maxsize=1)
        fps_queue = Queue(maxsize=1)

        cap = cv2.VideoCapture(video_path)
        
        Thread(target=video_capture, args=(cap, frame_queue, darknet_image_queue)).start()
        Thread(target=inference, args=(cap, args, darknet_image_queue, detections_queue, fps_queue)).start()
        Thread(target=drawing, args=(cap, self, args, frame_queue, detections_queue, fps_queue)).start()
        def keyPressEvent(self, e):
            if e.key() == Qt.Key_Escape:
                self.close()
                cap.release()
#----------------
#args = parser()


#frame_queue = Queue()
#darknet_image_queue = Queue(maxsize=1)
#detections_queue = Queue(maxsize=1)
#fps_queue = Queue(maxsize=1)
#--------------------



#model yolo로 대채됨
#network, class_names, class_colors = darknet.load_network(
#    args.config_file,
#    args.data_file,
#    args.weights,
#    batch_size=1
#)





def video_capture(cap, frame_queue, darknet_image_queue):
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #필요없을듯 ? 리사이즈 불필요
        #frame.shape[0]으로 높이 값 출력가능  # frame.shape = (높이, 너비, 채널) 예: (720, 1280, 3)
        #frame_resized = cv2.resize(frame_rgb, (416, 416),
        #                           interpolation=cv2.INTER_LINEAR)
        frame_queue.put(frame_rgb)
        
        #img_for_detect = model()
        #필요없는듯?

        #img_for_detect = darknet.make_image(width, height, 3)
        
        #darknet.copy_image_from_bytes(img_for_detect, frame_resized.tobytes())
        darknet_image_queue.put(frame_rgb)
    cap.release()

def inference(cap, args, darknet_image_queue, detections_queue, fps_queue):
    while cap.isOpened():
        darknet_image = darknet_image_queue.get()
        prev_time = time.time()
        detection = model(darknet_image)
        detections_queue.put(detection)
        fps = int(1 / (time.time() - prev_time))
        fps_queue.put(fps)
        print("FPS: {}".format(fps))
    cap.release()


#windwo sonmari.py에서 ui불러오는 것
def drawing(cap, window, args, frame_queue, detections_queue, fps_queue):
    random.seed(3)
    label = ""       #detect 결과(실시간으로 detect된 이미지)
    word = ""        #최종으로 출력할 단어
    sentence=[]      #출력할 문장
    
    result = ""          #현재 결과
    before_result = ""  #이전 결과
    result_que = Queue(3) #result들을 저장하는 큐 생성. 현재 결과까지 최대 3개 저장

    while cap.isOpen():
        frame_resized = frame_queue.get()
        detections = detections_queue.get()
        fps = fps_queue.get()

        if frame_resized is not None:
            for r in detections:

                annotator = Annotator(frame_resized)

                boxes = r.boxes
                for box in boxes:

                    b = box.xyxy[0]
                    c = box.cls
                    label = model.names[int(c)]
                    if label in list(one.keys()) :
                        annotator.box_label(b, one.get(label))
            hand_image = annotator.result()
        h, w, c = hand_image.shape
        qImg = QtGui.QImage(hand_image.data, w, h, w*c, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qImg)
        window.image.setPixmap(pixmap)

        if cv2.waitKey(fps) == 27:
            break
    cap.release()
    #video.release()
    cv2.destroyAllWindows()






#-------------------------------------
# Loop through the video frames
#while cap.isOpened():
#    # Read a frame from the video
#    success, frame = cap.read()
#
#    if success:
#        # Run YOLOv8 inference on the frame
#        results = model(frame)
#
#        # Visualize the results on the frame
#        annotated_frame = results[0].plot()
#
#        # Display the annotated frame
#        cv2.imshow("YOLOv8 Inference", annotated_frame)
#
#        # Break the loop if 'q' is pressed
#        if cv2.waitKey(1) & 0xFF == ord("q"):
#            break
#    else:
#        # Break the loop if the end of the video is reached
#        break
#----------------------------------------------------------------
# Release the video capture object and close the display window
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    sonmariWindow = MyApp() 

    #프로그램 화면을 보여주는 코드
    sonmariWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()

    sys.exit()
cv2.destroyAllWindows()
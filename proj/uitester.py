# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file '초안DFLBPx.ui'
## Created by: Qt User Interface Compiler version 6.7.0
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# 필요한 PySide6 모듈들을 임포트
from functools import partial
import cv2
from ultralytics import YOLO
from os import system
import argparse
from queue import Queue
import time
import random
from ultralytics.utils.plotting import Annotator  # ultralytics.yolo.utils.plotting is deprecated
from threading import Thread, enumerate

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGroupBox, QLabel, QProgressBar, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)
import sys  # 시스템 특정 파라미터와 함수를 작업하기 위해 필요

#model = YOLO('/home/taepark/goinfre/asdf.v1i.yolov8/runs/detect/train/weights/best.pt')
model = YOLO('yolov8n.pt')
#video_path = "/h`ome/taepark/goinfre/proj/123111.mp4"
#cap = cv2.VideoCapture(video_path)
#cap = cv2.VideoCapture(0)


one = {'person':'person output', 'cell phone':'cell phone out put', 'book':'book output'}

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



# 사용자 인터페이스 정의 클래스
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        # 대화 상자의 기본 설정
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(802, 500)  # 대화 상자 크기 설정

        # 답변 표시를 위한 프레임 설정
        self.answer_frame = QFrame(Dialog)
        self.answer_frame.setObjectName(u"answer_frame")
        self.answer_frame.setGeometry(QRect(20, 20, 341, 281))
        self.answer_frame.setFrameShape(QFrame.Shape.StyledPanel)  # 스타일 패널 형태
        self.answer_frame.setFrameShadow(QFrame.Shadow.Raised)  # 그림자 스타일

        # 답변 그룹박스 설정
        self.answer_group = QGroupBox(self.answer_frame)
        self.answer_group.setObjectName(u"answer_group")
        self.answer_group.setGeometry(QRect(10, 0, 321, 271))
        font = QFont()
        font.setFamilies([u"Monaco"])
        font.setPointSize(14)
        self.answer_group.setFont(font)  # 폰트 설정

        # 카라셀 위젯 (답변 이미지를 보여주는 부분)
        self.answer_carasel = QLabel(self.answer_group)
        self.answer_carasel.setObjectName(u"answer_carasel")
        self.answer_carasel.setGeometry(QRect(0, 20, 321, 251))
        #pixmap1 = QPixmap("C:\\git\\main\\proj\\proj\\person.png")
        #if pixmap1.isNull():
        #    print("이미지 로드 실패")
        #else:
        #    self.answer_carasel.setPixmap(pixmap1)
        #    print("이미지 로드 성공")
        #self.answer_carasel.setPixmap(pixmap1) 
        
        
        #self.answer_carasel.setPixmap(QPixmap())
        #print("이미지 제거됨")
        
        
    #----    
        
        #self.pixmap.load("1.png")
        #self.pixmap = self.pixmap.scaledToWidth(100)  # 이미지 크기 조정
        #self.answer_carasel.setPixmap(self.pixmap)
    #----

        # 비디오 표시를 위한 프레임 설정
        self.video_frame = QFrame(Dialog)
        self.video_frame.setObjectName(u"video_frame")
        self.video_frame.setGeometry(QRect(380, 20, 391, 281))
        self.video_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.video_frame.setFrameShadow(QFrame.Shadow.Raised)

        # 비디오 피드를 보여주는 라벨
        # 해결
        self.video_feed = QLabel(self.video_frame)
        self.video_feed.setObjectName(u"video_feed")
        self.video_feed.setGeometry(QRect(10, 10, 371, 261))

        # 진행 상황을 표시하는 프로그레스 바
        #해결
        self.progress_bar = QProgressBar(Dialog)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setGeometry(QRect(30, 410, 321, 23))
        self.progress_bar.setValue(24)  # 초기 값 설정

        # 문제 텍스트를 표시하는 프레임
        # 해결
        self.problem_frame = QFrame(Dialog)
        self.problem_frame.setObjectName(u"problem_frame")
        self.problem_frame.setGeometry(QRect(380, 320, 391, 121))
        self.problem_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.problem_frame.setFrameShadow(QFrame.Shadow.Raised)

        # 문제 그룹박스
        # 해결
        self.problem_group = QGroupBox(self.problem_frame)
        self.problem_group.setObjectName(u"problem_group")
        self.problem_group.setGeometry(QRect(10, 0, 371, 111))
        self.problem_group.setFont(font)  # 동일 폰트 사용

        # 문제 텍스트를 보여주는 텍스트 브라우저
        # 해결
        self.problem_word = QTextBrowser(self.problem_group)
        self.problem_word.setObjectName(u"problem_word")
        self.problem_word.setGeometry(QRect(0, 20, 371, 91))
        self.problem_word.setText("사람")

        # 정답 표시 체크박스
        self.show_answer = QCheckBox(Dialog)
        self.show_answer.setObjectName(u"show_answer")
        self.show_answer.setGeometry(QRect(20, 310, 71, 20))
        self.show_answer.setChecked(True)  # 프로그램 시작 시 체크박스를 체크된 상태로 설정
        png1 = "person"
        #self.image_names = ["1", "2", "3", "4", "5"]
        self.show_answer.stateChanged.connect(partial(self.onCheckboxStateChanged, png = png1))
        checked = self.show_answer.isChecked()
        print("체크박스 상태:", "Checked" if checked else "Unchecked")
        print("상태체크===== :::", checked)
        #self.show_answer.setChecked(True)
        #print("상태체크 on", checked)
        # 정답/오답 표시 라벨
        self.o_x_o = QLabel(Dialog)
        self.o_x_o.setObjectName(u"o_x_o")
        self.o_x_o.setGeometry(QRect(290, 310, 21, 41))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.o_x_o.setFont(font1)  # 폰트 스타일 설정

        # 오답 표시 라벨
        self.o_x_x = QLabel(Dialog)
        self.o_x_x.setObjectName(u"o_x_x")
        self.o_x_x.setGeometry(QRect(330, 310, 21, 41))
        self.o_x_x.setFont(font1)  # 동일 폰트 사용

        # 이전 문제 버튼
        self.previous_button = QPushButton(Dialog)
        self.previous_button.setObjectName(u"previous_button")
        self.previous_button.setGeometry(QRect(270, 450, 100, 32))

        # 다음 문제 버튼
        self.next_button = QPushButton(Dialog)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setGeometry(QRect(380, 450, 100, 32))

        self.retranslateUi(Dialog)  # UI 텍스트 설정 메서드 호출

        QMetaObject.connectSlotsByName(Dialog)  # 시그널과 슬롯을 자동으로 연결
        args = parser()

        frame_queue = Queue()
        darknet_image_queue = Queue(maxsize=1)
        detections_queue = Queue(maxsize=1)
        fps_queue = Queue(maxsize=1)

        #cap = cv2.VideoCapture(video_path)
        cap = cv2.VideoCapture(0)

        Thread(target=video_capture, args=(cap, frame_queue, darknet_image_queue)).start()
        Thread(target=inference, args=(cap, args, darknet_image_queue, detections_queue, fps_queue)).start()
        #Thread(target=drawing, args=(cap, self, args, frame_queue, detections_queue, fps_queue)).start()
        
    def onCheckboxStateChanged(self, state,png):
        print(f"State changed to: {state}")
        current_pixmap = self.answer_carasel.pixmap()

        print("시작전 -------- : ", current_pixmap)
        if state == 2:
            print("확인됨")
            #pixmap1 = QPixmap("C:\\git\\main\\proj\\proj\\person.png")
            base_image_path = "C:\\git\\main\\proj\\proj\\{}.png"
            image_path = base_image_path.format(png)  # 경로에서 숫자 부분을 i로 치환
            print(image_path) 
            pixmap1 = QPixmap(image_path)

            

            print("state == 2 :값이 뭐임? : ", current_pixmap)
            if pixmap1.isNull():
                print("이미지 로드 실패")
            else:
                self.answer_carasel.setPixmap(pixmap1)
                print("이미지 로드 성공")            
        else:
            print("----")   
            print("state == 0 :값이 뭐임? : ", current_pixmap)
            self.answer_carasel.setPixmap(QPixmap()) 
            print("^^^^^^초기화 후에 값은?? : ", current_pixmap)
    # setupUi

    def retranslateUi(self, Dialog):
        # 각 위젯의 텍스트 설정
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.answer_group.setTitle(QCoreApplication.translate("Dialog", u"정답", None))
        self.video_feed.setText("")
        self.answer_carasel.setText("")
        self.problem_group.setTitle(QCoreApplication.translate("Dialog", u"문제", None))
        self.show_answer.setText(QCoreApplication.translate("Dialog", u"정답 보기", None))
        
        #정답 오답시 생성되도록 변경해야 함
        self.o_x_o.setText(QCoreApplication.translate("Dialog", u"O", None))
        self.o_x_x.setText(QCoreApplication.translate("Dialog", u"X", None))
        
        self.previous_button.setText(QCoreApplication.translate("Dialog", u"이전 문제", None))
        self.next_button.setText(QCoreApplication.translate("Dialog", u"다음 문제", None))
    # retranslateUi

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

def drawing(cap, window, args, frame_queue, detections_queue, fps_queue):
    random.seed(3)
    label = ""       #detect 결과(실시간으로 detect된 이미지)
    word = ""        #최종으로 출력할 단어
    sentence=[]      #출력할 문장
    progress = 0
    result = ""          #현재 결과
    before_result = ""  #이전 결과
    result_que = Queue(3) #result들을 저장하는 큐 생성. 현재 결과까지 최대 3개 저장

    while cap.isOpened():
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
                    annotator.box_label(b, one.get(label))
            risized_hand_image = cv2.resize(annotator.result(), (371, 261), interpolation=cv2.INTER_AREA)
            #hand_image = annotator.result()
            hand_image = risized_hand_image#annotator.result()
            h, w, c = hand_image.shape
            qImg = QImage(hand_image.data, w, h, w*c, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qImg)
            window.video_feed.setPixmap(pixmap)
            pixmap1 = QPixmap("person.png")
            window.answer_carasel.setPixmap(pixmap1) 

            if cv2.waitKey(fps) == 27:
                break
    cap.release()
    #video.release()
    cv2.destroyAllWindows()







if __name__ == "__main__":
    app = QApplication(sys.argv)  # 애플리케이션 객체 생성
    Dialog = QDialog()  # 대화 상자 객체 생성
    ui = Ui_Dialog()  # UI 인스턴스 생성
    ui.setupUi(Dialog)  # UI 설정
    Dialog.show()  # 대화 상자 표시
    sys.exit(app.exec())  # 애플리케이션 실행

import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
import argparse
from queue import Queue

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


        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

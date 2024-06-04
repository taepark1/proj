import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QImage
import cv2
import os
import sys
from PyQt5 import QtWidgets, QtCore, QtGui

# 직접 플러그인 경로 지정
#os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '/home/taepark/goinfre/miniconda3/envs/newenv/lib/python3.8/site-packages/PyQt5/Qt5/plugins'

app = QtWidgets.QApplication(sys.argv)
# 앱의 나머지 부분을 여기에 추가

class MyApp(QtWidgets.QDialog):
    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi("sonmariui.ui", self)  # UI 파일 로드

        # 동영상 파일 로드
        self.cap = cv2.VideoCapture("11.mp4")  # 'video.mp4'를 여러분의 동영상 경로로 변경하세요.
        self.timer = QTimer(self)  # 프레임 업데이트를 위한 타이머
        self.timer.timeout.connect(self.update_frame)  # 타이머 시그널 연결
        self.timer.start(30)  # 33ms 간격으로 시그널 발생, 약 30fps

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # OpenCV는 이미지를 BGR 형식으로 처리하므로 RGB로 변환해야 함
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            p = convert_to_Qt_format.scaled(360, 400, Qt.KeepAspectRatio)
            self.image.setPixmap(QPixmap.fromImage(p))

#if __name__ == "__main__":
#    app = QtWidgets.QApplication(sys.argv + ['--platform', 'offscreen'])  # GUI 없이 작동
#    window = MyApp()
#    window.show()
#    sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

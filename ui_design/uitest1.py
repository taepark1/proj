# -*- coding: utf-8 -*-

from PySide6.QtCore import QCoreApplication, QTimer, QUrl
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QApplication, QDialog, QFrame, QLabel, QGroupBox, QPushButton, QProgressBar, QTextBrowser, QCheckBox, QWidget
import sys
import os

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(802, 500)
        
        # 이미지 표시 설정
        self.answer_frame = QFrame(Dialog)
        self.answer_frame.setGeometry(20, 20, 341, 281)
        self.answer_frame.setFrameShape(QFrame.StyledPanel)
        self.answer_group = QGroupBox("이미지", self.answer_frame)
        self.answer_group.setGeometry(10, 0, 321, 271)
        self.image_label = QLabel(self.answer_group)
        self.image_label.setGeometry(0, 20, 321, 251)
        self.image_label.setPixmap(QPixmap("1.png"))

        # 비디오 표시 설정
        self.video_frame = QFrame(Dialog)
        self.video_frame.setGeometry(380, 20, 391, 281)
        self.video_frame.setFrameShape(QFrame.StyledPanel)
        self.video_widget = QVideoWidget(self.video_frame)
        self.video_widget.setGeometry(10, 10, 371, 261)
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video_widget)
        self.player.setSource(QUrl.fromLocalFile(os.path.abspath("11.mp4")))
        self.player.play()

        # 기타 UI 요소
        self.progress_bar = QProgressBar(Dialog)
        self.progress_bar.setGeometry(30, 410, 321, 23)
        self.progress_bar.setValue(24)
        
        self.show_answer = QCheckBox("정답 보기", Dialog)
        self.show_answer.setGeometry(20, 310, 100, 20)
        
        self.o_x_o = QLabel("O", Dialog)
        self.o_x_o.setGeometry(290, 310, 21, 41)
        
        self.previous_button = QPushButton("이전", Dialog)
        self.previous_button.setGeometry(270, 450, 100, 32)
        self.next_button = QPushButton("다음", Dialog)
        self.next_button.setGeometry(380, 450, 100, 32)
        
        self.current_image_index = 0
        self.images = ["1.png", "2.png", "3.png", "4.png", "5.png"]
        
        self.previous_button.clicked.connect(self.previous_image)
        self.next_button.clicked.connect(self.next_image)

    def previous_image(self):
        self.current_image_index = (self.current_image_index - 1) % len(self.images)
        self.image_label.setPixmap(QPixmap(self.images[self.current_image_index]))

    def next_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.images)
        self.image_label.setPixmap(QPixmap(self.images[self.current_image_index]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

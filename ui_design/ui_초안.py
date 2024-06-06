# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '초안DFLBPx.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(802, 500)
        self.answer_frame = QFrame(Dialog)
        self.answer_frame.setObjectName(u"answer_frame")
        self.answer_frame.setGeometry(QRect(20, 20, 341, 281))
        self.answer_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.answer_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.answer_group = QGroupBox(self.answer_frame)
        self.answer_group.setObjectName(u"answer_group")
        self.answer_group.setGeometry(QRect(10, 0, 321, 271))
        font = QFont()
        font.setFamilies([u"Monaco"])
        font.setPointSize(14)
        self.answer_group.setFont(font)
        self.answer_carasel = QWidget(self.answer_group)
        self.answer_carasel.setObjectName(u"answer_carasel")
        self.answer_carasel.setGeometry(QRect(0, 20, 321, 251))
        self.video_frame = QFrame(Dialog)
        self.video_frame.setObjectName(u"video_frame")
        self.video_frame.setGeometry(QRect(380, 20, 391, 281))
        self.video_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.video_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.video_feed = QLabel(self.video_frame)
        self.video_feed.setObjectName(u"video_feed")
        self.video_feed.setGeometry(QRect(10, 10, 371, 261))
        self.progress_bar = QProgressBar(Dialog)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setGeometry(QRect(30, 410, 321, 23))
        self.progress_bar.setValue(24)
        self.problem_frame = QFrame(Dialog)
        self.problem_frame.setObjectName(u"problem_frame")
        self.problem_frame.setGeometry(QRect(380, 320, 391, 121))
        self.problem_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.problem_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.problem_group = QGroupBox(self.problem_frame)
        self.problem_group.setObjectName(u"problem_group")
        self.problem_group.setGeometry(QRect(10, 0, 371, 111))
        self.problem_group.setFont(font)
        self.problem_word = QTextBrowser(self.problem_group)
        self.problem_word.setObjectName(u"problem_word")
        self.problem_word.setGeometry(QRect(0, 20, 371, 91))
        self.show_answer = QCheckBox(Dialog)
        self.show_answer.setObjectName(u"show_answer")
        self.show_answer.setGeometry(QRect(20, 310, 71, 20))
        self.o_x_o = QLabel(Dialog)
        self.o_x_o.setObjectName(u"o_x_o")
        self.o_x_o.setGeometry(QRect(290, 310, 21, 41))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.o_x_o.setFont(font1)
        self.o_x_x = QLabel(Dialog)
        self.o_x_x.setObjectName(u"o_x_x")
        self.o_x_x.setGeometry(QRect(330, 310, 21, 41))
        self.o_x_x.setFont(font1)
        self.previous_button = QPushButton(Dialog)
        self.previous_button.setObjectName(u"previous_button")
        self.previous_button.setGeometry(QRect(270, 450, 100, 32))
        self.next_button = QPushButton(Dialog)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setGeometry(QRect(380, 450, 100, 32))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.answer_group.setTitle(QCoreApplication.translate("Dialog", u"\uc815\ub2f5", None))
        self.video_feed.setText("")
        self.problem_group.setTitle(QCoreApplication.translate("Dialog", u"\ubb38\uc81c", None))
        self.show_answer.setText(QCoreApplication.translate("Dialog", u"\uc815\ub2f5 \ubcf4\uae30", None))
        self.o_x_o.setText(QCoreApplication.translate("Dialog", u"O", None))
        self.o_x_x.setText(QCoreApplication.translate("Dialog", u"X", None))
        self.previous_button.setText(QCoreApplication.translate("Dialog", u"\uc774\uc804 \ubb38\uc81c", None))
        self.next_button.setText(QCoreApplication.translate("Dialog", u"\ub2e4\uc74c \ubb38\uc81c", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
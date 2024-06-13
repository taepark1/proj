# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_다양한컴포넌트EGBoLl.ui'
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
from PySide6.QtWidgets import (QApplication, QDial, QLCDNumber, QProgressBar,
    QScrollBar, QSizePolicy, QSlider, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(465, 480)
        self.dial = QDial(Form)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(140, 50, 151, 101))
        self.horizontalScrollBar = QScrollBar(Form)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setGeometry(QRect(40, 170, 371, 16))
        self.horizontalScrollBar.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(50, 210, 361, 25))
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 260, 371, 23))
        self.progressBar.setValue(24)
        self.lcdNumber = QLCDNumber(Form)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(80, 300, 281, 91))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi


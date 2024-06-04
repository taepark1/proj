import sys
from PyQt5.QtWidgets import *

class PushButtonWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        # 올바른 메서드 이름으로 변경
        self.setWindowTitle("Push Button Window")


        btn = QPushButton("Button", self)
        btn.move(150, 500)
        btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        QMessageBox.about(self, "Message", "Button Clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PushButtonWindow()
    window.show()
    app.exec_()
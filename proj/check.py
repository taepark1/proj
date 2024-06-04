import os
import sys
from PyQt5 import QtWidgets, uic, QtCore, QtGui

# 플러그인 경로 직접 설정
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '/home/taepark/goinfre/miniconda3/envs/newenv/lib/python3.8/site-packages/PyQt5/Qt/plugins'

# 애플리케이션 시작
app = QtWidgets.QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())

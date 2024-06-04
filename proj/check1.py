import sys
from PyQt5 import QtWidgets


app = QtWidgets.QApplication(sys.argv + ['--platform', 'offscreen'])
window = QtWidgets.QWidget()
window.setWindowTitle("Simple Test")
window.show()
sys.exit(app.exec_())

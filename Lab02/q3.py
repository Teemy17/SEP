import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import time

class Simple_timer_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.num = 0
        vbox = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText(str(self.num))
        vbox.addWidget(self.label)
        timer = QTimer(self)
        timer.timeout.connect(self.updateValue)
        timer.start(500)
        self.setLayout(vbox)
        self.show()

    def updateValue(self):
        current_time = time.strftime("%H:%M:%S")
        self.label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Simple_timer_window()
    sys.exit(app.exec())
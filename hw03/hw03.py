import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import time
from mainwindow import Ui_MainWindow

class ApplicationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.submit_button.clicked.connect(self.display_name)
        self.ui.timer = QTimer(self)
        self.ui.timer.timeout.connect(self.update_timer)
        self.ui.timer.start(1000)
        self.show()

    def update_timer(self):
        elapsed_time = time.strftime("%H:%M:%S")
        self.ui.timer_label.setText(elapsed_time)

    def display_name(self):
        user_name = self.ui.entry.toPlainText()
        if user_name:
            self.ui.name_label.setText(f"Hello, {user_name}!")
        else:
            self.ui.name_label.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ApplicationWindow()
    sys.exit(app.exec_())
import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class ApplicationWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Timer and Name Display")
        self.setGeometry(100, 100, 300, 200)

        vbox = QVBoxLayout()

        # Timer label
        self.timer_label = QLabel("00:00:00", self)
        font = self.timer_label.font()
        font.setPointSize(16)
        self.timer_label.setFont(font)
        self.timer_label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.timer_label)

        # Input label
        self.label = QLabel("Enter your name:", self)
        vbox.addWidget(self.label)

        # Text input field
        self.entry = QLineEdit(self)
        vbox.addWidget(self.entry)

        # Button
        self.btn = QPushButton("Submit", self)
        self.btn.clicked.connect(self.display_name)
        vbox.addWidget(self.btn)

        # Name display label
        self.name_label = QLabel("", self)
        self.name_label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.name_label)

        self.setLayout(vbox)

        # Timer setup
        self.start_time = QTime.currentTime()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)
        self.show()

    def update_timer(self):
        elapsed_time = time.strftime("%H:%M:%S")
        self.timer_label.setText(elapsed_time)

    def display_name(self):
        user_name = self.entry.text()
        if user_name:
            self.name_label.setText(f"Hello, {user_name}!")
        else:
            self.name_label.setText("Please enter your name.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ApplicationWindow()
    sys.exit(app.exec())
   
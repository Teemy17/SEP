import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Simple_spin_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.num = 0
        vbox = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText(str(self.num))
        vbox.addWidget(self.label)
        plus = QPushButton('+', self)
        plus.clicked.connect(self.updateNumber)
        vbox.addWidget(plus)
        minus = QPushButton('-', self)
        minus.clicked.connect(self.updateNumber)
        vbox.addWidget(minus)
        self.setLayout(vbox)
        reset = QPushButton('Reset', self)
        reset.clicked.connect(self.resetNumber)
        vbox.addWidget(reset)
        self.show()

    def updateNumber(self):
        button = self.sender()
        if button.text() == '+':
            self.num += 1
        else:
            self.num -= 1
        self.label.setText(str(self.num))

    def resetNumber(self):
        self.num = 0
        self.label.setText(str(self.num))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Simple_spin_window()
    sys.exit(app.exec())
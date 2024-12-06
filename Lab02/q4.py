import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Currency_converter(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.amount = 0
        self.rate = 0
        self.result = 0
        vbox = QVBoxLayout()
        self.label = QLabel(self)
        self.label.setText(str(self.result))
        vbox.addWidget(self.label)
        self.amount_input = QLineEdit(self)
        vbox.addWidget(self.amount_input)
        convert = QPushButton('THB to USD', self)
        convert.clicked.connect(self.thb_to_usd)
        vbox.addWidget(convert)
        convert2 = QPushButton('USD to THB', self)
        convert2.clicked.connect(self.usd_to_thb)
        vbox.addWidget(convert2)
        self.setLayout(vbox)
        self.show()

    def thb_to_usd(self):
        self.amount = float(self.amount_input.text())
        self.result = self.amount * 0.035
        self.label.setText(f"{self.result:.2f} USD")

    def usd_to_thb(self):
        self.amount = float(self.amount_input.text())
        self.result = self.amount * 35
        self.label.setText(f"{self.result:.2f} THB")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Currency_converter()
    sys.exit(app.exec())
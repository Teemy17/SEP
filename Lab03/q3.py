import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from program3_3 import Ui_MainWindow

class Dial_pad(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.press_button)
        self.ui.pushButton_2.clicked.connect(self.press_button)
        self.ui.pushButton_3.clicked.connect(self.press_button)
        self.ui.pushButton_4.clicked.connect(self.press_button)
        self.ui.pushButton_5.clicked.connect(self.press_button)
        self.ui.pushButton_6.clicked.connect(self.press_button)
        self.ui.pushButton_7.clicked.connect(self.press_button)
        self.ui.pushButton_8.clicked.connect(self.press_button)
        self.ui.pushButton_9.clicked.connect(self.press_button)
        self.ui.pushButton_10.clicked.connect(self.press_button)
        self.ui.pushButton_11.clicked.connect(self.press_button)
        self.ui.pushButton_12.clicked.connect(self.press_button)
        self.ui.pushButton_13.clicked.connect(self.press_dial)
        self.ui.pushButton_14.clicked.connect(self.press_backspace)
    
    def press_button(self):
        button = self.sender()
        self.ui.lineEdit.setText(self.ui.lineEdit.text() + button.text())

    def press_backspace(self):
        text = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(text[:-1])

    def press_dial(self):
        text = self.ui.lineEdit.text()
        self.ui.lineEdit.setText("Dialing " + text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dial_pad()
    window.show()
    sys.exit(app.exec_())
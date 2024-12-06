import sys
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, )

def say_hello():
    print("Hello, World!")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Simple")
    hello_button = QPushButton('Say hello!', window)
    hello_button.clicked.connect(say_hello)
    window.show()
    sys.exit(app.exec())
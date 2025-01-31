import js
from pyscript import document
from pyodide.ffi import create_proxy
from abc import ABC, abstractmethod
from datetime import datetime

class AbstractWidget(ABC):
    def __init__(self, element_id):
        self.element_id = element_id
        self._element = None

    @property
    def element(self):
        if not self._element:
            self._element = document.querySelector(f"#{self.element_id}")
        return self._element
    
    @abstractmethod
    def drawWidget(self):
        pass

    def getTime(self):
        return datetime.now().strftime("%H:%M:%S")
    
class NotificationWidget(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)

    def on_click(self, event):
        text = self.input_text.value
        js.alert("Hello " + text + " at " + self.getTime())

    def usd_to_thb(self, event):
        usd = self.input_text.value
        thb = float(usd) * 30
        js.alert("USD " + usd + " is THB " + str(thb))

    def thb_to_usd(self, event):
        thb = self.input_text.value
        usd = float(thb) / 30
        js.alert(f"{thb} THB is USD {usd:.2f}")

    def drawWidget(self):
        self.input_text = document.createElement("input", type="number")
        self.input_text.style.width = "600px"
        self.element.appendChild(self.input_text)

        self.button = document.createElement("button")
        self.button.innerText = "To THB"
        self.button.style.width = "600px"
        self.button.onclick = self.usd_to_thb
        self.element.appendChild(self.button)

        self.button = document.createElement("button")
        self.button.innerText = "To USD"
        self.button.style.width = "600px"
        self.button.onclick = self.thb_to_usd
        self.element.appendChild(self.button)

if __name__ == "__main__":
    output = NotificationWidget("container")
    output.drawWidget()
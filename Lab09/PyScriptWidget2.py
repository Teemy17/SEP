import js
from pyscript import document
from pyodide.ffi import create_proxy
from abc import ABC, abstractmethod

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

class AnimationWidget(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)
        self.counter = 1
        self.interval_id = None

    def on_click(self, event):
        if self.button.innerText == "Pause":
            self.button.innerText = "Play"
            js.window.clearInterval(self.interval_id)
        else:
            self.button.innerText = "Pause"
            self.interval_id = js.window.setInterval(create_proxy(self.on_setInterval), 100)

    def on_setInterval(self):
        self.counter += 1
        if self.counter > 20:
            self.jump_sound.play()
            self.counter = 1
        self.image.src = "./images/frame-" + str(self.counter) + ".png"

    def drawWidget(self):
        self.image = document.createElement("img")
        self.image.style.width = "600px"
        self.image.style.height = "600px"
        self.image.src = "./images/frame-1.png"
        self.element.appendChild(self.image)
        
        self.jump_sound = js.Audio.new("./sounds/rabbit_jump.wav")
        
        self.button = document.createElement("button")
        self.button.innerText = "Pause"
        self.button.style.width = "600px"
        self.button.onclick = create_proxy(self.on_click)
        self.element.appendChild(self.button)
        
        self.interval_id = js.window.setInterval(create_proxy(self.on_setInterval), 100)

class ColorfulAnimationWidget(AnimationWidget):
    def __init__(self, element_id):
        AnimationWidget.__init__(self, element_id)

    def random_color(self, event):
        r = js.Math.floor(js.Math.random() * 256)
        g = js.Math.floor(js.Math.random() * 256)
        b = js.Math.floor(js.Math.random() * 256)
        self.element.style.backgroundColor = f"rgb({r}, {g}, {b})"

    def drawWidget(self):
        AnimationWidget.drawWidget(self)
        self.button2 = document.createElement("button")
        self.button2.innerText = "Random Color"
        self.button2.style.width = "600px"
        self.button2.onclick = create_proxy(self.random_color)
        self.element.appendChild(self.button2)

if __name__ == "__main__":
    output = AnimationWidget("container")
    output2 = ColorfulAnimationWidget("container")
    output2.drawWidget()
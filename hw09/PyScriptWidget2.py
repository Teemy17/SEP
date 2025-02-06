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

class CharacterWidget(AbstractWidget):
    def __init__(self, element_id):
        super().__init__(element_id)
        self.counter = 1
        self.interval_id = None
        self.character = "rabbit"
        self.sounds = {
            "rabbit": "./sounds/rabbit_jump.wav",
            "run_gun": "./sounds/run_gun.mp3",
        }
    
    def on_click(self, event):
        if self.button.innerText == "Pause":
            self.button.innerText = "Play"
            js.window.clearInterval(self.interval_id)
        else:
            self.button.innerText = "Pause"
            self.interval_id = js.window.setInterval(create_proxy(self.on_setInterval), 100)
    
    def on_setInterval(self):
        self.counter += 1
        if self.counter > 8:
            self.play_sound()
            self.counter = 1
        self.image.src = f"./images/{self.character}{self.counter}.png"
    
    def play_sound(self):
        js.Audio.new(self.sounds[self.character]).play()
    
    def change_character(self, event):
        self.character = self.dropdown.value
        self.image.src = f"./images/{self.character}1.png"
    
    def drawWidget(self):
        self.image = document.createElement("img")
        self.image.style.width = "600px"
        self.image.style.height = "600px"
        self.image.src = "./images/rabbit1.png"
        self.element.appendChild(self.image)
        
        self.button = document.createElement("button")
        self.button.innerText = "Pause"
        self.button.style.width = "600px"
        self.button.onclick = create_proxy(self.on_click)
        self.element.appendChild(self.button)
        
        self.dropdown = document.createElement("select")
        for character in self.sounds.keys():
            option = document.createElement("option")
            option.value = character
            option.innerText = character.capitalize()
            self.dropdown.appendChild(option)
        self.dropdown.onchange = create_proxy(self.change_character)
        self.element.appendChild(self.dropdown)
        
        self.interval_id = js.window.setInterval(create_proxy(self.on_setInterval), 100)

class ColorButtonWidget(AbstractWidget):
    def drawWidget(self):
        self.button = document.createElement("button")
        self.button.innerText = "Random Color"
        self.button.style.width = "600px"
        self.button.onclick = create_proxy(self.random_color)
        self.element.appendChild(self.button)
    
    def random_color(self, event):
        r = js.Math.floor(js.Math.random() * 256)
        g = js.Math.floor(js.Math.random() * 256)
        b = js.Math.floor(js.Math.random() * 256)
        self.element.style.backgroundColor = f"rgb({r}, {g}, {b})"

class GreetingWidget(AbstractWidget):
    def drawWidget(self):
        self.input_box = document.createElement("input")
        self.input_box.type = "text"
        self.input_box.placeholder = "Enter your name"
        self.element.appendChild(self.input_box)
        
        self.button = document.createElement("button")
        self.button.innerText = "Greet"
        self.button.onclick = create_proxy(self.display_greeting)
        self.element.appendChild(self.button)
        
        self.output = document.createElement("p")
        self.element.appendChild(self.output)
    
    def display_greeting(self, event):
        user_name = self.input_box.value.strip()
        if user_name:
            self.output.innerText = f"Hello, {user_name}!"
        else:
            self.output.innerText = "Hello, stranger!"

if __name__ == "__main__":
    character_widget = CharacterWidget("container")
    character_widget.drawWidget()
    
    color_widget = ColorButtonWidget("container")
    color_widget.drawWidget()
    
    greeting_container = document.createElement("div")
    greeting_container.id = "greeting_container"
    document.body.appendChild(greeting_container)
    
    greeting_widget = GreetingWidget("greeting_container")
    greeting_widget.drawWidget()

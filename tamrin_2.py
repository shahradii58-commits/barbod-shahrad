from kivy.app import App
from kivy.uix.label import Label

class myapp(App):
    def build(self):
        label = Label(text="hello barbod and shahrad")
        return label
myapp().run()
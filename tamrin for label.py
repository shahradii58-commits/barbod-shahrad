from kivy.app import App
from kivy.uix.label import Label

class barbodapp(App):
    def build(self):
        label = Label(text="hello barbod and shahrad")
        return label
barbodapp().run()
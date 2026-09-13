from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class myapp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label1 = Label(text="hello barbod")
        label2 = Label(text="hello kivy!")
        layout.add_widget(label1)
        layout.add_widget(label2)
        return layout

myapp().run()
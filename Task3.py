from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        text = Label(text = "This is text")
        Btn = Button(text = "This is Button")
        layout = BoxLayout()
        layout.add_widget(text)
        layout.add_widget(Btn)
        return layout
    
MyApp().run()
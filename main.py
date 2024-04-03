from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox


class FirstScreen(Screen):
    def __init__(self, name = "first"):
        super().__init__(name = name)
        layout = BoxLayout()
        btntomainmenu = Button(text = "Go to main menu!")
        btntomainmenu.on_press = self.mainmenu
        self.i = 0
        self.txt = Label(text = "This is TEXT")
        btnclicker = Button(text=("This is BUTTON!!!"))
        btnclicker.on_press = self.change_text
        layout.add_widget(btntomainmenu)
        layout.add_widget(btnclicker)
        layout.add_widget(self.txt)
        self.add_widget(layout)


    def change_text(self):
        self.txt.text = str(self.i)
        self.i += 1


    def mainmenu(self):
        self.manager.transition.direction = "right"
        self.manager.current = "main"




class SecondScreen(Screen):
    def __init__(self, name = "second"):
        super().__init__(name = name)
        layout = BoxLayout()
        btntomainmenu = Button(text = "Go to main menu!")
        btntomainmenu.on_press = self.mainmenu
        self.i = 0
        self.txt = Label(text = "This is TEXT")
        btnclicker = Button(text=("This is BUTTON!!!"))
        btnclicker.on_press = self.change_text
        layout.add_widget(self.txt)
        layout.add_widget(btnclicker)
        layout.add_widget(btntomainmenu)
        self.add_widget(layout)


    def change_text(self):
        self.txt.text = str(self.i)
        self.i += 1


    def mainmenu(self):
        self.manager.transition.direction = "left"
        self.manager.current = "main"




class ThirdScreen(Screen):
    def __init__(self, name = "third"):
        super().__init__(name = name)
        layout = BoxLayout()
        btntomainmenu = Button(text = "Go to main menu!")
        btntomainmenu.on_press = self.mainmenu
        self.i = 0
        self.txt = Label(text = "This is TEXT")
        btnclicker = Button(text=("This is BUTTON!!!"))
        btnclicker.on_press = self.change_text
        layout.add_widget(btntomainmenu)
        layout.add_widget(btnclicker)
        self.add_widget(layout)
        layout.add_widget(self.txt)


    def change_text(self):
        self.txt.text = str(self.i)
        self.i += 1


    def mainmenu(self):
        self.manager.transition.direction = "right"
        self.manager.current = "main"


class FourthScreen(Screen):
    def __init__(self, name = "fourth"):
        super().__init__(name = name)
        layout = BoxLayout()
        btntomainmenu = Button(text = "Go to main menu!")
        btntomainmenu.on_press = self.mainmenu
        self.i = 0
        self.txt = Label(text = "This is TEXT")
        btnclicker = Button(text=("This is BUTTON!!!"))
        btnclicker.on_press = self.change_text
        layout.add_widget(self.txt)
        layout.add_widget(btnclicker)
        layout.add_widget(btntomainmenu)
        self.add_widget(layout)


    def change_text(self):
        self.txt.text = str(self.i)
        self.i += 1


    def mainmenu(self):
        self.manager.transition.direction = "left"
        self.manager.current = "main"
   
class MainScreen(Screen):
    def __init__(self, name = "main"):
        super().__init__(name = name)
        layout = BoxLayout(orientation = "vertical")
        btn = Button(text = "First Button!")
        btn.on_press = self.first
        btn2 = Button(text = "Second Button!")
        btn2.on_press = self.second
        btn3 = Button(text = "Third Button!")
        btn3.on_press = self.third
        btn4 = Button(text = "Fourth Button!")
        btn4.on_press = self.fourth
        layout.add_widget(btn)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        self.add_widget(layout)


    def first(self):
        self.manager.transition.direction = "left"
        self.manager.current = "first"


    def second(self):
        self.manager.transition.direction = "right"
        self.manager.current = "second"
   
    def third(self):
        self.manager.transition.direction = "left"
        self.manager.current = "third"


    def fourth(self):
        self.manager.transition.direction = "right"
        self.manager.current = "fourth"
       


   
class MyApp(App):
  def build(self):
    sm = ScreenManager()
    sm.add_widget(MainScreen())
    sm.add_widget(FirstScreen())
    sm.add_widget(SecondScreen())
    sm.add_widget(ThirdScreen())
    sm.add_widget(FourthScreen())
    return sm
 
MyApp().run()


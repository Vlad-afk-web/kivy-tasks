from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image
from kivy.uix.video import Video

class FirstScreen(Screen):

  def __init__(self, name="first"):
    super().__init__(name=name)

    layout = BoxLayout(orientation="vertical")
    btn = Button(text="Go to main menu")
    self.lable = Label(text="HUH", color= (1,0,0,1)) 
    wimg = Image(source='HUH.png')


    btn.on_press = self.main

    layout.add_widget(self.lable) 
    layout.add_widget(wimg)
    layout.add_widget(btn)

    self.add_widget(layout)

  def main(self):
    self.manager.transition.direction = "left"
    self.manager.current = "main"



  
class SecondScreen(Screen):

  def __init__(self, name="second"):
    super().__init__(name=name)

    layout = BoxLayout(orientation="vertical")
    btn = Button(text="Go to main menu")
    self.lable = Label(text="HUH", color= (1,0,0,1)) 
    wimg = Image(source='HUH.png')


    btn.on_press = self.main

    layout.add_widget(self.lable) 
    layout.add_widget(wimg)
    layout.add_widget(btn)

    self.add_widget(layout)

  def main(self):
    self.manager.transition.direction = "left"
    self.manager.current = "main"

def on_position_change(instance, value):
    print('The position in the video is', value)

def on_duration_change(instance, value):
    print('The duration of the video is', value)

video = Video(source='PandaSneezes.avi')
video.bind(
    position=on_position_change,
    duration=on_duration_change
)


class ThirdScreen(Screen):

  def __init__(self, name="third"):
    super().__init__(name=name)

    checkbox = CheckBox()
    layout = BoxLayout(orientation="vertical")
    btn = Button(text="Go to main menu")
    self.lable = Label(text="CheckBox - Disable \n This is third screen", color= (1,0,0,1))

    btn.on_press = self.main
    checkbox.bind(active=self.on_checkbox_active)

    layout.add_widget(self.lable)
    layout.add_widget(checkbox)
    layout.add_widget(btn)

    self.add_widget(layout)

  def main(self):
    self.manager.transition.direction = "left"
    self.manager.current = "main"

  def on_checkbox_active(self, checkbox, value):  
    if value:
      self.lable.text = "CheckBox - Active \n Third screen" 
      self.lable.color = (0, 1, 0, 1)
    else:
      self.lable.text = "CheckBox - Disable \n Third screen"
      self.lable.color = (1, 0, 0, 1)



class FourScreen(Screen):

  def __init__(self, name="four"):
    super().__init__(name=name)

    checkbox = CheckBox()
    layout = BoxLayout(orientation="vertical")
    btn = Button(text="Go to main menu")
    self.lable = Label(text="CheckBox - Disable \n This is fourth screen", color= (1,0,0,1))

    btn.on_press = self.main
    checkbox.bind(active=self.on_checkbox_active)

    layout.add_widget(self.lable)
    layout.add_widget(checkbox)
    layout.add_widget(btn)

    self.add_widget(layout)

  def main(self):
    self.manager.transition.direction = "left"
    self.manager.current = "main"

  def on_checkbox_active(self, checkbox, value):  
    if value:
      self.lable.text = "CheckBox - Active \n Fourth screen" 
      self.lable.color = (0, 1, 0, 1)
    else:
      self.lable.text = "CheckBox - Disable \n Fourth screen"
      self.lable.color = (1, 0, 0, 1)



class MainScreen(Screen):

  def __init__(self, name="main"):
    super().__init__(name=name)

    layout = BoxLayout(orientation="vertical")

    btnf = Button(text="Go to first screen")
    layout.add_widget(btnf)

    btns = Button(text="Go to second screen")
    layout.add_widget(btns)

    btnt = Button(text="Go to third screen")
    layout.add_widget(btnt)

    btnff = Button(text="Go to fourth screen")
    layout.add_widget(btnff)

    btnff.on_press = self.four
    btnt.on_press = self.third
    btns.on_press = self.second
    btnf.on_press = self.first

    self.add_widget(layout)

  def first(self):
    self.manager.transition.direction = "up"
    self.manager.current = "first"

  def second(self):
    self.manager.transition.direction = "down"
    self.manager.current = "second"

  def third(self):
    self.manager.transition.direction = "left"
    self.manager.current = "third"

  def four(self):
    self.manager.transition.direction = "right"
    self.manager.current = "four"

#__________________________________________________________________________________________________________________________________________
class MyApp(App):

  def build(self):
    sm = ScreenManager()
    sm.add_widget(MainScreen())
    sm.add_widget(FirstScreen())
    sm.add_widget(SecondScreen())
    sm.add_widget(ThirdScreen())
    sm.add_widget(FourScreen())
    return sm


MyApp().run()
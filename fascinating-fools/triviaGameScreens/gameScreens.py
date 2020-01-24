from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, FadeTransition, Screen



class StartTriviaHomeLayout(Screen):
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(StartTriviaHomeLayout, self).__init__(**kwargs)


class SoundButton(Button):
    def __init__(self, sound_file, **kwargs):
        super(SoundButton, self).__init__(**kwargs)
        self.sound = SoundLoader.load(sound_file)
        self.category = self.text
    def play(self):
        self.sound.play()

class FirstGridRow(BoxLayout):
    pass

class SecondGridRow(BoxLayout):
    pass

class ThirdGridRow(BoxLayout):
    pass

class FourthGridRow(BoxLayout):
    pass

def handle_category_selection(self, pressed):
    pressed.play_sound()
    pass
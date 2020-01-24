from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty


class StartTriviaHomeLayout(Screen):
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        super(StartTriviaHomeLayout, self).__init__(**kwargs)

    def handle_category_selection(self, categoryName):
        self.manager.current = "home_screen"



class SoundButton(Button):
    sound_file = StringProperty('assets/button-press-whoosh.wav')
    def on_press(self):
        sound = SoundLoader.load(self.sound_file)
        sound.play()


class FirstGridRow(BoxLayout):
    pass

class SecondGridRow(BoxLayout):
    pass

class ThirdGridRow(BoxLayout):
    pass

class FourthGridRow(BoxLayout):
    pass


class TriviaCategoryScreen(Screen):
    category = StringProperty('UnknownCategory')
    def go_back_home(self):
        self.manager.current = "start_page"
    def press_start_button(self):
        self.manager.current = "play_screen"

class PlayScreen(Screen):
    pass

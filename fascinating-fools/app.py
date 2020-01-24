from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from triviaGameScreens import gameScreens


class TriviaGame(App):
    """
        documentation here.
    """
    def build(self):
        """

            :return:
        """
        screen_manager = ScreenManager(transition=FadeTransition())
        Builder.load_file(
            "kvFiles/StartTriviaHomeLayout.kv"
        )
        screen_manager.add_widget(
            gameScreens.StartTriviaHomeLayout(name='start_page')
        )
        return screen_manager




if __name__ == '__main__':
    TriviaGame().run()

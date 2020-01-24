from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from triviaGameScreens import gameScreens

global screen_manager
screen_manager = ScreenManager(transition=FadeTransition())


class TriviaGame(App):
    """
        documentation here.
    """
    def build(self):
        """

            :return:
        """
        Builder.load_file(
            "kvFiles/StartTriviaHomeLayout.kv"
        )
        Builder.load_file(
            "kvFiles/TriviaCategoryScreen.kv"
        )
        Builder.load_file(
            "kvFiles/PlayScreen.kv"
        )
        screen_manager.add_widget(
            gameScreens.StartTriviaHomeLayout(name='start_page')
        )
        screen_manager.add_widget(
            gameScreens.TriviaCategoryScreen(name="home_screen")
        )
        screen_manager.add_widget(
            gameScreens.PlayScreen(name="play_screen")
        )
        return screen_manager




if __name__ == '__main__':
    TriviaGame().run()

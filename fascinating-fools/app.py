from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from triviaGameScreens import gameScreens
from triviaGameObjects.quiz import Quiz

import json
import os

class TriviaScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        ScreenManager.__init__(self, **kwargs)
        # Will be set after the quiz category was selected
        self.quiz_category: str = ""
        self.active_quiz: Quiz = None

    def load_questions_for_category(self, category: str):
        json_file_path = f"triviaQuestions/{category}.json"
        assert os.path.isfile(json_file_path), f"Selected category was {category}, but file {json_file_path} could not be found."
        with open(json_file_path) as f:
            return json.load(f)


class TriviaGame(App):
    """
        documentation here.
    """

    def __init__(self, **kwargs):
        App.__init__(self, **kwargs)
        self.screen_manager = TriviaScreenManager(transition=FadeTransition())

    def build(self):
        """
            :return:
        """
        Builder.load_file("kvFiles/StartTriviaHomeLayout.kv")
        Builder.load_file("kvFiles/TriviaCategoryScreen.kv")
        Builder.load_file("kvFiles/PlayScreen.kv")

        self.screen_manager.add_widget(
            gameScreens.StartTriviaHomeLayout(name="start_page")
        )
        self.screen_manager.add_widget(
            gameScreens.TriviaCategoryScreen(name="home_screen")
        )
        self.screen_manager.add_widget(gameScreens.PlayScreen(name="play_screen"))
        return self.screen_manager


if __name__ == "__main__":
    TriviaGame().run()

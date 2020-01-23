import kivy
from kivy.app import App
from kivy.uix.label import Label


class TriviaGame(App):
    """
        documentation here.
    """
    def build(self):
        """

            :return:
        """
        return Label(text='trivia game to be implemented')


if __name__ == '__main__':
    TriviaGame().run()

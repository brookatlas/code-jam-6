from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.clock import Clock

from triviaGameObjects.quiz import Quiz

from typing import List


class StartTriviaHomeLayout(Screen):
    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        Screen.__init__(self, **kwargs)

    def handle_category_selection(self, categoryName):
        self.manager.quiz_category = categoryName
        self.manager.current = "home_screen"


class SoundButton(Button):
    sound_file = StringProperty("assets/button-press-whoosh.wav")

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
    category = StringProperty("UnknownCategory")

    def go_back_home(self):
        self.manager.current = "start_page"

    def press_start_button(self):
        quiz_questions = self.manager.load_questions_for_category(
            self.manager.quiz_category
        )
        self.manager.active_quiz = Quiz(quiz_questions)
        self.manager.current = "play_screen"


class PlayScreen(Screen):
    def __init__(self, **kw):
        Screen.__init__(self, **kw)
        # While the transition is active, the player should not be able to select the answer before the question is visible
        self.locked = False

    def on_pre_enter(self, *args):
        """ Called when animation starts. """
        # See events: https://kivy.org/doc/stable/api-kivy.uix.screenmanager.html?highlight=screen#kivy.uix.screenmanager.Screen
        # Update the strings on the new scene, e.g. label and buttons text
        self.setup_question_text()
        self.setup_answer_text()
        self.locked = True

    def on_enter(self, *args):
        """ Called when animation is completed."""
        self.locked = False

    def setup_question_text(self):
        """ Set up the question label text. """
        self.children[0].children[4].text = self.manager.active_quiz.question_title

    def setup_answer_text(self):
        """ Set up the answer text and change button background to default color. """
        answers: List[str] = self.manager.active_quiz.answers
        # Fourth answer has index 0, first answer has index 3
        for i, answer in enumerate(answers):
            self.children[0].children[3 - i].text = answer
            # After highlighting wrong and correct answers, change the background color to default color
            self.children[0].children[3 - i].background_color = [1, 1, 1, 1]

    def highlight_correct_answer(self):
        """ Highlight correct answer in green. """
        correct_answer_index = self.manager.active_quiz.correct_answer_index
        self.children[0].children[3 - correct_answer_index].background_color = [
            0,
            255,
            0,
            100,
        ]

    def highlight_wrong_answer(self, selected_answer: int):
        """ Highlight wrong answer in red. """
        self.children[0].children[3 - selected_answer].background_color = [
            255,
            0,
            0,
            100,
        ]

    def answer_button_pressed(self, pressed_button_index: int):
        if not self.locked:
            self.highlight_correct_answer()
            answer_is_correct = self.manager.active_quiz.answer(pressed_button_index)
            if not answer_is_correct:
                self.highlight_wrong_answer(pressed_button_index)
            # TODO: sleep for 1-5 seconds (highlight correct answer and wrong answer), then display next question
            #   perhaps fade out the current scene, then fade it back in and display new

            quiz_is_done = self.manager.active_quiz.quiz_done
            # TODO if quiz is completed, change screne to 'quiz is over' or 'quiz summary' scene and show summary of how well the player did, which answers were correctly answered and which wrong
            # self.manager.current = "summary_screen"

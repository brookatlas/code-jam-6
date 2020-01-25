from typing import List


class Quiz:
    """
        documentation here.
    """

    def __init__(self, questions):
        # See 'triviaQuestions' folder for the structure of the quiz
        self.questions = questions["questions"]
        self.question_index = 0
        self.right_answers = 0
        self.wrong_answers = 0
        self.chosen_answer_index = 0
        self.quiz_done = False

    @property
    def question_title(self) -> str:
        return self.questions[self.question_index]["question"]

    @property
    def answers(self) -> List[str]:
        return self.questions[self.question_index]["answers"]

    @property
    def correct_answer_index(self) -> int:
        return self.questions[self.question_index]["correct_answer_index"]

    @property
    def correct_answer(self) -> str:
        return self.questions[self.question_index]["answers"]

    def is_quiz_done(self):
        """
        checks if the quiz instance was done by the user
        :return: a boolean, indicating if the quiz has been done.
        """
        return self.quiz_done

    def get_current_question(self):
        """
        gets the question object of the current question in the quiz
        :return:
        a question object of the current question in the quiz
        """
        return self.questions[self.question_index]

    def answer(self, answer_index):
        """
            answers a question of the quiz.
            if the answer is right, the quiz moves
        :param answer_text:
            a text of the answer
        :return:
        """
        correct_answer_index = self.correct_answer_index
        if len(self.questions) == self.question_index + 1:
            self.quiz_done = True
        else:
            self.question_index += 1

        if answer_index == correct_answer_index:
            self.right_answers += 1
            return True
        else:
            self.wrong_answers += 1
            return False

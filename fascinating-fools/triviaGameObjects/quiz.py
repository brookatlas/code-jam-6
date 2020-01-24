
class quiz:
    '''
        documentation here.
    '''
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_index = 0
        self.right_answers = 0
        self.wrong_answers = 0
        self.chosen_answer_index = 0
        self.quiz_done = False

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
        return self.question_list[self.question_index]

    def answer(self, answer_index):
        """
            answers a question of the quiz.
            if the answer is right, the quiz moves
        :param answer_text:
            a text of the answer
        :return:
        """
        if self.quiz_done:
            return None
        is_answer_right = self.question_list[self.question_index].answer(answer_index)
        if len(self.question_list) == (self.question_index + 1):
            self.quiz_done = True
        else:
            self.question_index += 1
        if is_answer_right:
            self.right_answers += 1
            return True
        else:
            self.wrong_answers += 1
            return False
        return None
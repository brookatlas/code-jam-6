
class question:
    '''
        documentation here
    '''
    def __init__(self, question_text, answer_list):
        self.question_text = question_text
        self.answer_list = answer_list

    def get_answer_by_text(self, answer_text):
        """
            gets an answer from the quiz, by the matching answer_text iself
        :param answer_text:

        :return:
        """
        for answer in self.answer_list:
            if(answer.get_answer_text() == answer_text):
                return answer
        return None

    def answer(self, answer_text):
        matching_answer = self.get_answer_by_text(answer_text)
        if matching_answer.is_answer_right():
            return True
        return False

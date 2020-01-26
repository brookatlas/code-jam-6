class Answer:
    """
        documentation here.
    """

    def __init__(self, answer_text, is_right):
        self.answer_text = answer_text
        self.isRight = is_right

    def get_answer_text(self):
        return self.answer_text

    def is_answer_right(self):
        return self.isRight

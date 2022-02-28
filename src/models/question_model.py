class QuestionModel:
    def __init__(self, question, options, rightAnswer, pathImage=None, pathVideo=None):
        self.question = question
        self.options = options
        self.rightAnswer = rightAnswer
        self.pathImage = pathImage
        self.pathVideo = pathVideo

    def toJson(self):
        return {
            'question': self.question,
            'options': self.options,
            'rightAnswer': self.rightAnswer,
            'pathImage': self.pathImage,
            'pathVideo': self.pathVideo
        }

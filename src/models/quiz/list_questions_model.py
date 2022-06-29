class ListQuestionsModel:

    def __init__(self, questions):
        self.questions = questions

    def toJson(self):
        listQuestions = []
        for question in self.questions:
            listQuestions.append(question.toJson())
        return listQuestions

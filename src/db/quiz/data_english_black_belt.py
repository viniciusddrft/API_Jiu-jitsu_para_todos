
from src.models.quiz.list_questions_model import ListQuestionsModel
from src.models.quiz.question_model import QuestionModel


dataEnglishBlackBelt = ListQuestionsModel([
    QuestionModel(
        question='What was the first family to challenge the Gracie family?',
        options=['Almeida', 'Machida', 'Fadda', 'Machado'],
        rightAnswer='Fadda'
    ),
    QuestionModel(
        question='Which year did the jiu-jitsu come to Brazil?',
        options=['1914', '1913', '1915', '1910'],
        rightAnswer='1914'
    ),
    QuestionModel(
        question='Which year the CBJJ was establish?',
        options=['1994', '1993', '1992', '1990'],
        rightAnswer='1994'
    ),
    QuestionModel(
        question='Which was the first woman to get the black belt?',
        options=['Yvone Duarte', 'kyra Graice',
                 'Bianca Basilio', 'Beatriz Mesquita'],
        rightAnswer='Yvone Duarte'
    ),
    QuestionModel(
        question='Which year was the first world cup of jiu-jitsu?',
        options=['1995', '1996', '1997', '1998'],
        rightAnswer='1996'
    ),
    QuestionModel(
        question='Which year was the first jiu-jitsu world cup out of Brazil?',
        options=['2004', '2005', '2006', '2007'],
        rightAnswer='2007'
    ),
])

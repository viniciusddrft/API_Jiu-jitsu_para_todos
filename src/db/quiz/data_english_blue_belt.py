
from src.models.quiz.list_questions_model import ListQuestionsModel
from src.models.quiz.question_model import QuestionModel


dataEnglishBlueBelt = ListQuestionsModel([
    QuestionModel(
        question='What brazilian fighter did can overtake Royce Grace in the UFC completions?',
        options=['Conor McGregor', 'Anderson Silva',
                 'Charles do Bronx', 'Demian Maia'],
        rightAnswer='Charles do Bronx'
    ),
    QuestionModel(
        question='What’s the name of the jiu-jitsu style that the fight without gi?',
        options=['Submission', 'Subjitsu', 'Jiu-jitsu without gi', 'Absolute'],
        rightAnswer='Submission'
    ),
    QuestionModel(
        question='What one of this attacks is forbidden in blue belt?',
        options=['Leg lock', 'Straight footlock', 'Kimura', 'Americana'],
        rightAnswer='Leg lock'
    ),
    QuestionModel(
        question='What is the minimal age to get the black belt?',
        options=['18', '19', '20', '21'],
        rightAnswer='19'
    ),
    QuestionModel(
        question='Which one of these moves is forbidden in jiu-jitsu according to the CBJJ rules?',
        options=['Slam', 'Shoulder blade', 'Biceps lock', 'Calf lock'],
        rightAnswer='Slam'
    ),
])

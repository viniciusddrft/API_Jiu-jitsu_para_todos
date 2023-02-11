
from src.models.quiz.list_questions_model import ListQuestionsModel
from src.models.quiz.question_model import QuestionModel


dataEnglishWhiteBelt = ListQuestionsModel([
    QuestionModel(
        question='How much scores does the throw gives?',
        options=['2', '3', '4', '5'],
        rightAnswer='2'
    ),
    QuestionModel(
        question='Which belt comes before brown?',
        options=['Purple', 'Blue', 'Green', 'Black'],
        rightAnswer='Purple'
    ),
    QuestionModel(
        question='What means “jiu-jitsu”?',
        options=['Soft art', 'Fight art',
                 'Empty hands', 'Combat art'],
        rightAnswer='Soft art'
    ),
    QuestionModel(
        question='Which family did give a beginning to jiu-jitsu in Brazil?',
        options=['Gracie', 'Machida',
                 'Fadda', 'Machado'],
        rightAnswer='Gracie'
    ),
    QuestionModel(
        question='Which belt comes after brown?',
        options=['Purple', 'Blue', 'Green', 'Black'],
        rightAnswer='Black'
    ),
    QuestionModel(
        question='Which country did the jiu-jitsu has origin?',
        options=['Japan', 'India', 'Brazil', 'Australia'],
        rightAnswer='India'
    ),
    QuestionModel(
        question='How is denominated who fights jiu-jitsu?',
        options=['Fighter', 'Jiujiteiro', 'Jiujitsuka', 'Judoka'],
        rightAnswer='Jiujitsuka'
    ),
    QuestionModel(
        question='What’s the last belt of jiu-jitsu?',
        options=['Red', 'Black', 'Red and Black', 'Silver'],
        rightAnswer='Red'
    ),
    QuestionModel(
        question='How much scores does the guard pass gives?',
        options=['2', '3', '4', '5'],
        rightAnswer='3'
    ),
])

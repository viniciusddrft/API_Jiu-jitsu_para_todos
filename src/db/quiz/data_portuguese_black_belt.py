
from src.models.quiz.list_questions_model import ListQuestionsModel
from src.models.quiz.question_model import QuestionModel


dataPortugueseBlackBelt = ListQuestionsModel([
    QuestionModel(
        question='Qual foi a primeira familia a desafiar a fámilia gracie?',
        options=['Família Almeida', 'Familia Machida',
                 'Familia Fadda', 'Família Machado'],
        rightAnswer='Familia Fadda'
    ),
    QuestionModel(
        question='Qual ano que o jiu-jitsu chegou ao brasil?',
        options=['1914', '1913', '1915', '1910'],
        rightAnswer='1914'
    ),
    QuestionModel(
        question='Em qual ano a CBJJ foi fundada?',
        options=['1994', '1993', '1992', '1990'],
        rightAnswer='1994'
    ),
    QuestionModel(
        question='Qual foi a primeira mulher a pegar a faixa preta?',
        options=['Yvone Duarte', 'kyra Graice',
                 'Bianca Basílio', 'Beatriz Mesquita'],
        rightAnswer='Yvone Duarte'
    ),
    QuestionModel(
        question='Em que ano foi o primeiro mundial de Jiu-jitsu?',
        options=['1995', '1996', '1997', '1998'],
        rightAnswer='1996'
    ),
    QuestionModel(
        question='Em que ano foi o primeiro mundial de Jiu-jitsu fora do Brasil?',
        options=['2004', '2005', '2006', '2007'],
        rightAnswer='2007'
    ),
])

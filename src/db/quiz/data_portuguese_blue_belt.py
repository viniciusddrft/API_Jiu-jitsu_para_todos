
from src.models.quiz.list_questions_model import ListQuestionsModel
from src.models.quiz.question_model import QuestionModel


dataPortugueseBlueBelt = ListQuestionsModel([
    QuestionModel(
        question='Qual lutador brasileiro que conseguiu ultrapassar Royce Gracieem finalizações no UFC?',
        options=['Conor McGregor', 'Anderson Silva',
                 'Charles do Bronx', 'Demian Maia'],
        rightAnswer='Charles do Bronx'
    ),
    QuestionModel(
        question='Qual o Nome do estilo de jiu jitsu cuja luta é feita sem kimono?',
        options=['Submission', 'Subjitsu', 'Jiu-jitsu sem kimono', 'Absoluto'],
        rightAnswer='Submission'
    ),
    QuestionModel(
        question='Qual desses ataques é proibido na faixa azul?',
        options=['Leg lock', 'Chave de pé reta', 'Kimura', 'Americana'],
        rightAnswer='Leg lock'
    ),
    QuestionModel(
        question='Qual a idade miníma para pegar a faixa preta?',
        options=['18', '19', '20', '21'],
        rightAnswer='19'
    ),
    QuestionModel(
        question='Qual desses movimentos é proibido no jiu-jitsu segundo as regras da CBJJ?',
        options=['Bate estaca', 'Omoplata',
                 'Chave de bíceps', 'Chave de panturrilha'],
        rightAnswer='Bate estaca'
    ),
])

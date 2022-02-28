
from src.models.list_questions_model import ListQuestionsModel
from src.models.question_model import QuestionModel


dataPortugueseWhiteBelt = ListQuestionsModel([
    QuestionModel(
        question='Quantos pontos vale uma queda?',
        options=['2', '3', '4', '5'],
        rightAnswer='2'
    ),
    QuestionModel(
        question='Qual faixa vem antes da marrom?',
        options=['Roxa', 'Azul', 'Verde', 'Preta'],
        rightAnswer='Roxa'
    ),
    QuestionModel(
        question='O que significa Jiu-jitsu?',
        options=['Arte suave', 'Arte da luta',
                 'Mãos vazias', 'Arte do combate'],
        rightAnswer='Arte suave'
    ),
    QuestionModel(
        question='Qual família deu inicio no jiu-jitsu no brasil?',
        options=['Família Gracie', 'Família Machida',
                 'Família Fadda', 'Família Machado'],
        rightAnswer='Família Gracie'
    ),
    QuestionModel(
        question='Qual faixa vem depois da marrom?',
        options=['Roxa', 'Azul', 'Verde', 'Preta'],
        rightAnswer='Preta'
    ),
    QuestionModel(
        question='Em qual pais o jiu-jitsu teve origem?',
        options=['Japão', 'India', 'Brasil', 'Austrália'],
        rightAnswer='India'
    ),
    QuestionModel(
        question='Quem luta Jiu-Jitsu é denominado como?',
        options=['Lutador', 'Jiujiteiro', 'Jiujitsuka', 'Judoca'],
        rightAnswer='Jiujitsuka'
    ),
    QuestionModel(
        question='Qual a ultima faixa do Jiu-Jitsu?',
        options=['Vermelha', 'Preta', 'Coral', 'Prata'],
        rightAnswer='Vermelha'
    ),
    QuestionModel(
        question='Quantos pontos vale uma passagem de guarda?',
        options=['2', '3', '4', '5'],
        rightAnswer='3'
    ),
])

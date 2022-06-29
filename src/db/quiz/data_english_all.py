from src.db.quiz.data_english_white_belt import dataEnglishWhiteBelt
from src.db.quiz.data_english_blue_belt import dataEnglishBlueBelt
from src.db.quiz.data_english_black_belt import dataEnglishBlackBelt

dataEnglishAll = []
dataEnglishAll.append(dataEnglishWhiteBelt.toJson())
dataEnglishAll.append(dataEnglishBlueBelt.toJson())
dataEnglishAll.append(dataEnglishBlackBelt.toJson())

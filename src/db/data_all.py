from src.db.data_portuguese_white_belt import dataPortugueseWhiteBelt
from src.db.data_portuguese_blue_belt import dataPortugueseBlueBelt
from src.db.data_portuguese_black_belt import dataPortugueseBlackBelt
from src.db.data_english_white_belt import dataEnglishWhiteBelt
from src.db.data_english_blue_belt import dataEnglishBlueBelt
from src.db.data_english_black_belt import dataEnglishBlackBelt

dataAll = []
dataAll.append(dataPortugueseWhiteBelt.toJson())
dataAll.append(dataPortugueseBlueBelt.toJson())
dataAll.append(dataPortugueseBlackBelt.toJson())
dataAll.append(dataEnglishWhiteBelt.toJson())
dataAll.append(dataEnglishBlueBelt.toJson())
dataAll.append(dataEnglishBlackBelt.toJson())

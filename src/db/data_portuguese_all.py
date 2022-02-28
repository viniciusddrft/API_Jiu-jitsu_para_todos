from src.db.data_portuguese_white_belt import dataPortugueseWhiteBelt
from src.db.data_portuguese_blue_belt import dataPortugueseBlueBelt
from src.db.data_portuguese_black_belt import dataPortugueseBlackBelt

dataPortugueseAll = []
dataPortugueseAll.append(dataPortugueseWhiteBelt.toJson())
dataPortugueseAll.append(dataPortugueseBlueBelt.toJson())
dataPortugueseAll.append(dataPortugueseBlackBelt.toJson())


from utils import Data

d = Data()


while True:
    _ = input("Press Enter to collect datapoint")
    datapoint = {"415nm": 1,
                 "445nm": 2,
                 "480nm": 3,
                 "515nm": 4,
                 "555nm": 5,
                 "590nm": 6,
                 "630nm": 7,
                 "680nm": 8
                 }
    d.add(datapoint)
    print(d.make_smooth_dataset().T)


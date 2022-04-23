import numpy as np

import pandas as pd

data = np.array([1,2,3,4,5,6,7])
print(data)

s = pd.Series(data, index=data)
print(s)

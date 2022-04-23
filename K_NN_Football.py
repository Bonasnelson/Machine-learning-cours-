import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv('vgsales.csv')

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)



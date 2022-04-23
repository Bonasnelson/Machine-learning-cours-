import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import scatter
from  sklearn import  svm


# visualization of dataset
import matplotlib.pylab as plt
import  seaborn as sns; sns.set(font_scale = 1.2)

recipes = pd.read_csv('C:\SCHOOL\Data science\Data\dataset.csv')
#print(recipes.head())

# plot the data
#sns.lmplot(x='Dribbling', y='Finishing', data =recipes, palette='Set1', fit_reg = False, scatter_kws={"s":70})
#plt.show()
for r in recipes.values:
    if r[1] =='Lionel Messi':
       print(r)

#print(recipes['Name'].values)

import numpy as np
from sklearn import preprocessing,cross_validation,neighbors
import pandas as import pd

df=pd.read_csv('')

df.replace('?', -99999,inplace=True)

df.drop(['id'],1,inplace=True)

x=np.array(df.drop('class',1))
y=np.array(df['class'])

x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size=0.2)
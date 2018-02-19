import pandas as pd
import quandl 
import math

df=quandl.get('WIKI/GOOGL')


df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume', ]]
df['HCL_PCT']=(df['Adj. High']-df['Adj. Close'])/df['Adj. Close']*100.0
df['PCT_Change']=(df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']*100.0

df= df[['Adj. Close','HCL_PCT','PCT_Change','Adj. Volume',]]

forecast= 'Adj.Close'
df.fillna(-9999, inplace=True)

forecast_out=int(math.ceil(0.01*len(df)))

df['label']=df[forecast].shift(-forecast_out)
df.dropna(inplace=True)

print(df.head())
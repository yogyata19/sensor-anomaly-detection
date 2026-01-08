import pandas as pd
df=pd.read_csv("data/sensor.csv")
print(df.head(10))
print(df.info())
print(df.describe())
print(df.isnull().sum())
df['anomaly']=False
#data driven anomaly detection
temp_mean=df['temp'].mean()
temp_std=df['temp'].std()
temp_upper=temp_mean +2*temp_std
temp_lower=temp_mean-2*temp_std
df.loc[(df['temp']>temp_upper)|(df['temp']<temp_lower),'anomaly']=True
print(df['anomaly'].value_counts())
#Z-score calc for temp
df["z_score_temp"]=(df['temp']-temp_mean)/temp_std
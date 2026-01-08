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
import matplotlib.pyplot as plt
#seperating  normal and anomalous points
normal_data=df[df['anomaly']==False]
anomaly_data=df[df['anomaly']==True]
plt.figure(figsize=(10,5))
#plot normal temperature
plt.plot(normal_data['ts'],
         normal_data['temp'],
         label="normal",
         color="green")
#plot anomalies
plt.scatter(anomaly_data['ts'],
            anomaly_data['temp'],
            color='yellow',
            label='Anomaly')
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Temperature Sensor Data with Anomalies")
plt.legend()
plt.show() 
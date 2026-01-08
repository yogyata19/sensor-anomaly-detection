import pandas as pd
import matplotlib.pyplot as plt
def load_data(path):
    """Load sensor dataset from CSV file"""
    return pd.read_csv(path)
def detect_temperature_anomalies(df):
    """Detect temperature anomalies using Z-score"""
    temp_mean=df['temp'].mean()
    temp_std=df['temp'].std()
    df["z_score_temp"]=(df['temp']-temp_mean)/temp_std
    df['anomaly'] = (df['z_score_temp'].abs() > 2)

    return df
def visualize_temp(df):
    """Visualize normal and anomalous temperature readings"""
    #seperating  normal and anomalous points
    normal_data=df[df['anomaly']==False]
    anomaly_data=df[df['anomaly']==True]
    #plot normal temperature
    plt.plot(normal_data['ts'],
         normal_data['temp'],
         label="normal",
         color="red")
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
df=load_data("data/sensor.csv")
df= detect_temperature_anomalies(df)
visualize_temp(df)

    

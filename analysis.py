import pandas as pd
import matplotlib.pyplot as plt
def load_data(path):
    """Load sensor dataset from CSV file"""
    
    return pd.read_csv(path)
    df['ts']=pd.to_datetime(df['ts'],unit='s')
def detect_anomalies(df,column):
    """Detect sensor anomalies using Z-score"""
    mean=df[column].mean()
    std=df[column].std()
    df[f'z_score_{column}']=(df[column]-mean)/std
    df[f'anomaly_{column}'] = (df[f'z_score_{column}'].abs() > 3)

    return df
def visualize_sensor(df,column):
    """Visualize normal and anomalous  readings"""
    #seperating  normal and anomalous points
    normal_data=df[df[f'anomaly_{column}']==False]
    anomaly_data=df[df[f'anomaly_{column}']==True]
    plt.figure(figsize=(10,5))
    #plot normal temperature
    plt.plot(normal_data['ts'],
         normal_data[column],
         label="normal",
         color="blue")
    #plot anomalies
    plt.scatter(anomaly_data['ts'],
            anomaly_data[column],
            color='red',
            label='Anomaly')
    plt.xlabel("Time")
    plt.ylabel(column.capitalize())
    plt.title(f"{column.capitalize()} Sensor Data with Anomalies")
    plt.legend()
    plt.show() 
if __name__=="__main__" :   
    df=load_data("data/sensor.csv")
df= detect_anomalies(df,'temp')
df=detect_anomalies(df,'humidity')
visualize_sensor(df,'humidity')
visualize_sensor(df,'temp')

    

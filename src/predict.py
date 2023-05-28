import pandas as pd
from sklearn.neighbors import BallTree
import numpy as np
from src.utils import calculate_distance

def EstimatedTravelTime(df, dfInput):
    """
    Function to estimate travel time.
    
    Args:
        df: Pandas dataframe containing BMTC data.
        dfInput: Pandas dataframe containing input data.
    
    Returns:
        dfOutput: Pandas dataframe containing the output.
    """

    test = dfInput.copy()
    dfOutput = pd.DataFrame()
    
    # Extract time information from Timestamp column
    tstamp = df['Timestamp'].astype("string").str.split(' ',expand=True)
    tstamp = tstamp.drop(0,axis=1)
    tstamp = tstamp[1].astype("string").str.split(':',expand=True)
    tstamp = tstamp.astype(int)
    
    # Calculate time in minutes from the start time
    df["Time"] = tstamp[0]*60 + tstamp[1] + tstamp[2]*(1/60)
    df["Time"] = df["Time"] - df["Time"][0]
    df = df.drop("Timestamp",axis=1)
    
    # Get unique bus IDs
    busid = df["BusID"].unique()
    
    # Prepare data for time and distance reports
    test_s = test.drop(["Dest_Lat","Dest_Long"],axis=1)
    test_d = test.drop(["Source_Lat","Source_Long"],axis=1)

    time_report = test.copy()
    time_report = time_report.drop(["Source_Lat","Source_Long","Dest_Lat","Dest_Long"],axis=1)

    dist_report = test.copy()
    dist_report = dist_report.drop(["Source_Lat","Source_Long","Dest_Lat","Dest_Long"],axis=1)

    # Calculate distances using calculate_distance function
    dist = calculate_distance(test["Source_Lat"],test["Source_Long"],test["Dest_Lat"],test["Dest_Long"])
    tt = []
    
    for i in busid:
        bus = df[(df["BusID"]==i)]
        X = bus.drop(["BusID","Speed","Time"],axis=1)
        bt = BallTree(X,metric='haversine')
        KNN = 8
        if (len(bus) < KNN):
             KNN = len(bus)
        
        # Calculate nearest neighbors
        _ , s = bt.query(test_s,k=KNN)
        _ , d = bt.query(test_d,k=KNN)
    
        # Calculate time differences
        time = pd.DataFrame()
        DD = pd.DataFrame(np.array(bus["Time"])[d])
        SS = pd.DataFrame(np.array(bus["Time"])[s])
        for p in range(KNN):
            for q in range(KNN):
                time[(p+1)*(q+1)] = DD[p] - SS[q]
        time[(time<=0)] = 100000
        time = time.T.min()
        time_report = pd.concat([time_report, time], axis=1)        
    
        # Calculate latitude and longitude differences
        lat_d = pd.DataFrame(np.array(bus["Latitude"])[d]).T.min()
        lat_s = pd.DataFrame(np.array(bus["Latitude"])[s]).T.min()
    
        long_d = pd.DataFrame(np.array(bus["Longitude"])[d]).T.min()
        long_s = pd.DataFrame(np.array(bus["Longitude"])[s]).T.min()    
    
        d_d = calculate_distance(lat_d, long_d, test["Dest_Lat"], test["Dest_Long"])
        d_s = calculate_distance(lat_s, long_s, test["Source_Lat"], test["Source_Long"])
        t_d = d_d + d_s
        dist_report = pd.concat([dist_report, t_d], axis=1)
    
    # Create a de-fragmented copy of the DataFrame
    time_report_copy = time_report.copy()
    dist_report_copy = dist_report.copy()
    
    for k in range(len(test)):
        loc = ((5*dist_report_copy.iloc[k] + 1*dist_report_copy.iloc[k]*time_report_copy.iloc[k]) == 
               (5*dist_report_copy.iloc[k] + 1*dist_report_copy.iloc[k]*time_report_copy.iloc[k]).min())
        t = time_report_copy.iloc[k][loc]    
        t = t + dist_report_copy.iloc[k][loc]*6
        tt.append(np.array(t))
    dfOutput = np.array(tt)

    return dfOutput 

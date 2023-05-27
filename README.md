# CNI Hackathon 2022

Background
We have a dataset containing information about the buses travelling in Bengaluru. We have obtained it from Bengaluru Metropolitan Transport Corporation (BMTC).
The region of interest is an approximately 40km by 40km square area. See the following figure:

The data was collected from around two thousand buses for one day, between 7:00am to 7:00pm.
The buses follow different routes within the city.
Each bus is identified with a unique ID. A bus carries a device which records the data: latitude, longitude, speed, and timestamp.
Task
Create a model to estimate the travel time, in minutes, between source-destination pairs using the provided dataset.

Dataset
We are providing the following three files in the dataset (download link ):

BMTC.parquet.gzip: It contains the GPS traces of around two thousand buses.
Input.csv: It contains geographical coordinates of various sources-destination pairs.
GroundTruth.csv: It contains the ground truth travel times between the source-destination pairs provided in Input.csv. It is provided to help participants assess their solutions.
Following is the detailed description of the contents of these files:
BMTC.parquet.gzip:
The file contains information in five columns, described as follows:
BusID: The (unique) ID associated with the device present in a bus.
Latitude: Latitude (geographical coordinate) of a bus, as recorded by the device.
Longitude: Longitude (geographical coordinate) of the bus, as recorded by the device.
Speed: Instantaneous speed of the bus in kmph.
Timestamp: Timestamp in IST format. The format of datetime is yyyy-mm-dd HH:MM:SS.
For better understanding, following is a snapshot from the dataset:

BusID	Latitude	Longitude	Speed	Timestamp
0	150212121	13.06593	77.45269	20	2019-08-01 18:59:18
1	150212121	13.06627	77.45211	27	2019-08-01 18:59:28
2	150212121	13.06661	77.45152	24	2019-08-01 18:59:38
3	150212121	13.06697	77.45089	28	2019-08-01 18:59:48
4	150212121	13.06727	77.45035	26	2019-08-01 18:59:58
5	150218000	13.00571	77.68619	46	2019-08-01 07:22:33
6	150218000	13.00525	77.68542	35	2019-08-01 07:22:42
7	150218000	13.00504	77.68509	0	2019-08-01 07:22:51
8	150218000	13.00504	77.68509	0	2019-08-01 07:23:01
9	150218000	13.00498	77.68497	13	2019-08-01 07:23:11
Note: The devices may not record the data with same sampling intervals. The recordings may also be noisy.

Input.csv:
The file contains four columns, described as follows:
Source_Lat: The latitude of a source.
Source_Long: The longitude of a source.
Dest_Lat: The latitude of a destination.
Dest_Long: The longitude of a destination.
For better understanding, following is the format of a typical input file:

Source_Lat	Source_Long	Dest_Lat	Dest_Long
0	13.067272	77.45035	13.00525	77.68542
1	13.005042	77.68509	13.06627	77.45211
2	13.065925	77.45269	13.00498	77.68497
3	13.005247	77.68542	13.06661	77.45152
GroundTruth.csv:
The file contains one column TT, i.e. the actual travel time between a source-destination pair. The value in the i-th row corresponds to the travel time between i-th source-destination pair in Input.csv.

For better understanding, following is the format of a typical ground truth file:

TT
0	1.99
1	6.21
2	7.34
3	5.20
You can use the ground truth from the dataset to check if your code is working well.

Output (Estimated Travel Time)
Your output will be the estimated travel time (ETT), in minutes, between a given source-destination pair. For each source-destination pair, you should fill this value in the ETT column of a pandas dataframe, as illustrated below:

# CNI HACKATHON 2022

This repository contains the necessary files and instructions to create a model for estimating the travel time between source-destination pairs using a dataset of bus GPS traces.

## Background

We have obtained a dataset from the Bengaluru Metropolitan Transport Corporation (BMTC) that contains information about buses traveling in Bengaluru. The dataset includes GPS traces of approximately two thousand buses within an approximately 40km by 40km square area. The data was collected for one day, between 7:00am to 7:00pm. Each bus is identified with a unique ID and carries a device that records latitude, longitude, speed, and timestamp.

## Task

The task is to create a model that can estimate the travel time, in minutes, between source-destination pairs using the provided dataset.

## Dataset

The dataset consists of the following three files, which can be downloaded using the provided link:

1. `BMTC.parquet.gzip`: This file contains the GPS traces of around two thousand buses. It includes information about each bus's ID, latitude, longitude, speed, and timestamp.

2. `Input.csv`: This file contains geographical coordinates of various source-destination pairs.

3. `GroundTruth.csv`: This file contains the ground truth travel times between the source-destination pairs provided in `Input.csv`. It can be used to assess the performance of the created model.

For a detailed description of the contents of these files, please refer to the dataset documentation.

## Usage

To estimate the travel time between source-destination pairs, follow these steps:

1. Download the dataset files (`BMTC.parquet.gzip`, `Input.csv`, and `GroundTruth.csv`) using the provided download link.

2. Set up the necessary dependencies and libraries, including Python and the required Python packages (e.g., Pandas, NumPy, scikit-learn).

3. Load the dataset files into your program using the appropriate libraries (e.g., Pandas).

4. Train a travel time estimation model using the provided dataset.

5. Evaluate the performance of the model by comparing the estimated travel times with the ground truth travel times from `GroundTruth.csv`.

6. Adjust and refine the model as necessary to improve its accuracy.

7. Use the trained model to estimate travel times for new source-destination pairs by providing the coordinates as input and retrieving the estimated travel time as output.

8. Store the estimated travel times in a Pandas DataFrame with the column name "ETT" (Estimated Travel Time).

## Example DataFrame

Your output should be in the form of a Pandas DataFrame, with the estimated travel times (ETT) filled in the "ETT" column. Here's an example:

```
   Source_Lat  Source_Long  Dest_Lat  Dest_Long   ETT
0   13.067272    77.450350  13.00525   77.68542  6.59
1   13.005042    77.685090  13.06627   77.45211  7.81
2   13.065925    77.452690  13.00498   77.68497  8.94
3   13.005247    77.685420  13.06661   77.45152  6.80
```

Please replace the "ETT" values with your estimated travel times.

## License

The dataset and this project are provided under the [MIT License](LICENSE.md).

Feel free to explore the dataset, create and improve upon the model, and share your insights with the community. Good luck!

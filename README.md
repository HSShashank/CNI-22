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

Feel free to explore the dataset, create and improve upon the model, and share your insights with the community. Good luck!

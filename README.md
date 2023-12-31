# data-pipeline-drugs-test
Build a data pipeline to search for different drugs into the different clinical trials and pubmed in order to get which drug is mentioned in which trial, when, which journal ...

## Installation

Prerequisites
- Docker Desktop
- Docker account

## Project structure

The python project is constructed like the following:
- **data directory**: contains the three csv files
  - clinical_trials.csv
  - drugs.csv
  - pubmed.csv

- **read input files** (_read_input_files.py_): read the csv files into a pandas dataframe
- **Preprocessing step**  (_preprocessing_data.py_): cleans the data (null values, duplicates, date format, lower characters, ... )
- **Processing step** (_processing_data.py_): 
  - contains functions to search for the different drugs in the different pubmed and clinical trials and generates a json file as output.
  - function max_journal: which journal has the maximum drugs mentioned
- **main file**: (_drug_analyzer.py_): the main file that runs all the previous steps
- **Dockerfile:** generates the first docker image "sma/drug_analyzer:v1" 

- **Parameters file** (_Parameters.txt_): contains three parameters that you may change/update:
  - DATE_FORMATS: the different date_formats that you want to change in the files
  - DESIRED_FORMAT: the desired date format that you want to get for all the date types
  - FILE_PATH: the path and file name that you want to store your output json file in

## Execution steps

1. Install Docker Desktop 
https://docs.docker.com/desktop/install/windows-install/

2. Create an account on Docker if you don't have one already

3. Pull the docker image for my project. To do so, run these commands in you cmd terminal:

`docker pull sma/drug_analyzer:v1`

This will get you the image in your docker space.

4. You need to run the docker image to generate container thus run the application.

`docker run sma/drug_analyzer:v1`

You may be able to get the json file as output.

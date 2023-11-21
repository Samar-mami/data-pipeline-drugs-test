from preprocessing_data import *
from read_input_files import *

clinical_trials = read_csv_file("data/clinical_trials.csv", 0, ',')
drugs = read_csv_file("data/drugs.csv", 0, ',')
pubmed = read_csv_file("data/pubmed.csv", 0, ',')
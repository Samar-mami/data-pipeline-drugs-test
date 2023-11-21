from read_input_files import *
from preprocessing_data import *

# read csv input files
df_clinical_trials = read_csv_file("data/clinical_trials.csv", 0, ',')
df_drugs = read_csv_file("data/drugs.csv", 0, ',')
df_pubmed = read_csv_file("data/pubmed.csv", 0, ',')

# read parameters file
parameters_file = 'parameters.txt'
params = read_parameters_file(parameters_file)

# Access individual parameters
date_formats = params.get('DATE_FORMATS', [])
desired_format = params.get('DESIRED_FORMAT', '')

# Modify date format to get the same data format for all dataframes
df_clinical_trials['date'] = df_clinical_trials['date'].apply(
    lambda x: parse_and_reformat(x, date_formats=date_formats, desired_format=desired_format))
df_pubmed['date'] = df_pubmed['date'].apply(
    lambda x: parse_and_reformat(x, date_formats=date_formats, desired_format=desired_format))

fill_na_df(df_clinical_trials)
fill_na_df(df_pubmed)
fill_na_df(df_drugs)
drop_duplicates_df(df_clinical_trials)
drop_duplicates_df(df_pubmed)
drop_duplicates_df(df_drugs)

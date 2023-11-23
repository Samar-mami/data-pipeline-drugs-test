from read_input_files import *
from preprocessing_data import *
from processing_data import *


def get_file_path(parameters_file):
    params = read_parameters_file(parameters_file)
    return params.get('FILE_PATH', '')


def main():
    """
        entry point to run the drug analyzer app.
    """
    print("Welcome to my drug analyser app :) !\n")
    # read csv input files
    df_clinical_trials = read_csv_file("data/clinical_trials.csv", 0, ',')
    df_drugs = read_csv_file("data/drugs.csv", 0, ',')
    df_pubmed = read_csv_file("data/pubmed.csv", 0, ',')

    # Apply preprocessing operations on the different dataframes
    df_clinical_trials = preprocess_df(df_clinical_trials)
    df_drugs = preprocess_df(df_drugs)
    df_pubmed = preprocess_df(df_pubmed)

    # process data: find the drug name in the different pubmed, clinical trials and journals
    df_clinical_trials_search = find_drug_name(df_drugs, 'drug', df_clinical_trials, 'scientific_title')

    df_pubmed_search = find_drug_name(df_drugs, 'drug', df_pubmed, 'title')

    final_result = merge_dataframes(df_clinical_trials_search, df_pubmed_search, 'drug')

    # rename different columns for a better comprehensible result
    final_result.columns = final_result.columns.str.replace('_x', '_clinical_trial')
    final_result.columns = final_result.columns.str.replace('_y', '_pubmed')

    json_result = convert_df_to_json(final_result)
    # pretty_json = json.dumps(json_result)
    print("Here's the final result in json format... !")
    print(json_result)
    # Specify the file path where you want to store the JSON file
    file_path = get_file_path('parameters.txt')
    # Now you can use the 'file_path' variable in your code
    print("file have been stored to:", file_path)
    # Write the JSON string to a file
    with open(file_path, "w") as json_file:
        json_file.write(json_result)

    max_journal(file_path)

if __name__ == '__main__':
    main()

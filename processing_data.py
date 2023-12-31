import pandas as pd
import json
from collections import Counter


def find_drug_name(df_reference: pd, reference_name_column: str, df_search_in: pd, title_search_in_column: str):
    df_found = pd.DataFrame(columns=['drug', 'referenced_in', 'date_mention', 'journal'])
    for drug in df_reference[f'{reference_name_column}']:
        for title in df_search_in[f'{title_search_in_column}']:
            if drug in title:
                index = df_search_in[df_search_in[f'{title_search_in_column}'] == title].index[0]
                # Append the data to df_found
                row = [drug, title, df_search_in.loc[index, 'date'], df_search_in.loc[index, 'journal']]
                df_found.loc[len(df_found)] = row
    return df_found


def merge_dataframes(df1, df2, merge_column):
    try:
        print("Merging Dataframes on: "f'{merge_column}', "...")
        final_df = pd.merge(df1, df2, on=f'{merge_column}')
        return final_df
    except Exception as e:
        print("An error has occurred: "f'{e}')


def convert_df_to_json(df):
    try:
        print("Converting Dataframe to json...")
        json = df.to_json(orient='records')
        return json
    except Exception as e:
        print("An error has occurred: "f'{e}')


def max_journal(json_file):
    # Load data from the corrected JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Extract drug names and journals
    # drug_names = [entry['drug'] for entry in data]
    journals = [entry['journal_pubmed'] for entry in data]  # + [entry['journal_clinical_trials'] for entry in data]
    # Count occurrences of each journal
    journal_counts = Counter(journals)

    # Find the journal with the maximum count
    maxi_journal, max_count = journal_counts.most_common(1)[0]

    # Print the result
    print(f"The journal with the maximum drug name citations is '{maxi_journal}' with {max_count} citations.")

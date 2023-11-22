import pandas as pd


def find_drug_name(df_drugs, drug_name_column, df_search, title_column):
    df_found = pd.DataFrame(columns=['drug', 'referenced_in', 'date_mention'])
    for drug in df_drugs[f'{drug_name_column}']:
        for title in df_search[f'{title_column}']:
            if drug in title:
                date_index = df_search[df_search[f'{title_column}'] == title].index[0]
                # Append the data to df_found
                row = [drug, title, df_search.loc[date_index, 'date']]
                df_found.loc[len(df_found)] = row
    return df_found

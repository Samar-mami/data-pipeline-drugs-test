import pandas as pd


def find_drug_name(df_reference, referance_name_column, df_search_in, title_search_in_column):
    df_found = pd.DataFrame(columns=['drug', 'referenced_in', 'date_mention'])
    for drug in df_reference[f'{referance_name_column}']:
        for title in df_search_in[f'{title_search_in_column}']:
            if drug in title:
                date_index = df_search_in[df_search_in[f'{title_search_in_column}'] == title].index[0]
                # Append the data to df_found
                row = [drug, title, df_search_in.loc[date_index, 'date']]
                df_found.loc[len(df_found)] = row
    return df_found


def merge_dataframes(df1, def2, merge_column):
    try:
        print("Merging Dataframes on: "f'{merge_column}', "...")
        final_df = pd.merge(df1, df1, on=f'{merge_column}')
        return final_df
    except Exception as e:
        print("An error has occurred: "f'{e}')


def convert_df_to_json(df):
    try:
        print("Converting Dataframe to json...")
        json = df.to_json()
        return json
    except Exception as e:
        print("An error has occurred: "f'{e}')

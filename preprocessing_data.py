import pandas as pd


# Function to parse and reformat dates
def parse_and_reformat(date_str, date_formats, desired_format):
    try:
        for fmt in date_formats:
            try:
                parsed_date = pd.to_datetime(date_str, format=fmt)
                # Reformat the parsed date to the desired format
                parsed_date.strftime(desired_format)
                # return reformatted_date
            except ValueError:
                pass
        # If none of the formats match, return None
        return None
    except Exception as e:
        print(f"Error processing date {date_str}: {e}")
        return None


# fillna
def fill_na_df(df):
    df.fillna('')
    print('Null values have been replaced with an empty string !')


# drop duplicates if exists
def drop_duplicates_df(df):
    if df.duplicated().any():
        df.drop_duplicates(inplace=True)
        print('Duplicates have been removed !')


# lower all the colums in the dataframe
def lower_df(df):
    try:
        df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
        print('Lower function has been applied correctly !')
    except Exception as e:
        print(f"An exception occured: {e}")
    finally:
        print(df.head())


# replace unneccessary caracters
def clean_df(df, column):
    try:
        df[f'{column}'] = df[f'{column}'].str.replace('[^a-zA-Z0-9 ]', '', regex=True)
        print("Dataframe is cleaned !")
    except Exception as e:
        print(f"An exception occured: {e}")


def rename_columns(df, column, new_column):
    df.rename(columns={f'{column}': new_column}, inplace=True)
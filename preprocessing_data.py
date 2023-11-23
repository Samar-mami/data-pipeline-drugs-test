import pandas as pd

from read_input_files import read_parameters_file


# Function to parse and reformat dates
def parse_and_reformat(date_str, date_formats, desired_format):
    try:
        for fmt in date_formats:
            try:
                parsed_date = pd.to_datetime(date_str, format=fmt)
                # Reformat the parsed date to the desired format
                reformatted_date = parsed_date.strftime(desired_format)
                return reformatted_date
            except ValueError:
                pass
        # If none of the formats match, return None
        return None
    except Exception as e:
        print(f"Error processing date {date_str}: {e}")
        return None


# filling null values with an empty string
def fill_na_df(df):
    df.fillna('', inplace=True)
    print('Null values have been replaced with an empty string !')


# drop duplicates if exists
def drop_duplicates_df(df):
    if df.duplicated().any():
        df.drop_duplicates(inplace=True)
        print('Duplicates have been removed !')


# lower all the columns in the dataframe
def lower_df(df):
    try:
        df = df.map(lambda x: x.lower() if isinstance(x, str) else x)
        print('Lower function has been applied correctly !')
        return df
    except Exception as e:
        print(f"An exception occurred: {e}")


# replace unnecessary characters
def clean_df(df, column):
    try:
        df[f'{column}'] = df[f'{column}'].str.replace('[^a-zA-Z0-9 ]', '', regex=True)
        print("Dataframe is cleaned !")
    except Exception as e:
        print(f"An exception occurred: {e}")


def rename_columns(df, column, new_column):
    df.rename(columns={f'{column}': new_column}, inplace=True)


def preprocess_df(df):
    # read parameters file
    parameters_file = 'parameters.txt'
    params = read_parameters_file(parameters_file)
    # Access individual parameters
    date_formats = params.get('DATE_FORMATS', [])
    desired_format = params.get('DESIRED_FORMAT', '')

    # Modify date format to get the same data format for all dataframes
    if 'date' in df.columns:
        print("Formatting date...")
        df['date'] = df['date'].apply(
            lambda x: parse_and_reformat(x, date_formats=date_formats, desired_format=desired_format))
    fill_na_df(df)
    drop_duplicates_df(df)
    df = lower_df(df)
    return df

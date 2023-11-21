import pandas as pd


def read_csv_file(path, header, sep):
    try:
        df = pd.read_csv(path, header=header, sep=sep)
        print('csv file read successfully !')
        print(df.head())
        return df
    except FileNotFoundError:
        print(f"Error: The file '{path}' does not exist !")
    except pd.errors.ParserError as e:
        print(f"Error parsing csv: {e}")



import pandas as pd


def read_csv_file(path, header, sep):
    try:
        df = pd.read_csv(path, header=header, sep=sep)
        print(f'{path}', ' file read successfully !')
        print(df.head())
        return df
    except FileNotFoundError:
        print(f"Error: The file '{path}' does not exist !")
    except pd.errors.ParserError as e:
        print(f"Error parsing csv: {e}")


def read_parameters_file(parameters_file):
    # Initialize a dictionary to store parameters
    parameters = {}
    try:
        # Read the parameter file
        with open(parameters_file, 'r') as file:
            for line in file:
                # Split each line into key and value
                key, value = line.strip().split('=')
                # Parse the value using eval
                parameters[key] = eval(value)
        # Print the extracted values (for verification)
        # for key, value in parameters.items():
        # print(f"{key}: {value}")
    except FileNotFoundError:
        print(f"Error: File '{parameters_file}' not found.")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
    return parameters

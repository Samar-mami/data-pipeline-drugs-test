
# Function to parse and reformat dates
def parse_and_reformat(date_str):
    try:
        # Try to parse the date using multiple formats
        date_formats = ['%d/%m/%Y', '%d-%m-%Y', '%Y-%m-%d', '%d %B %Y']
        for fmt in date_formats:
            try:
                parsed_date = pd.to_datetime(date_str, format=fmt)
                # Reformat the parsed date to the desired format
                reformatted_date = parsed_date.strftime('%d/%m/%Y')
                return reformatted_date
            except ValueError:
                pass
        # If none of the formats match, return None
        return None
    except Exception as e:
        print(f"Error processing date {date_str}: {e}")
        return None


# fillna
clinical_trials.fillna('')
# drop duplicates if exists
if pubmed.duplicated().any():
    pubmed.drop_duplicates(inplace=True)
# lower
clinical_trials = clinical_trials.applymap(lambda x: x.lower() if isinstance(x, str) else x)
# replace unneccessary caracters
clinical_trials['scientific_title'] = clinical_trials['scientific_title'].str.replace('[^a-zA-Z0-9 ]', '', regex=True)

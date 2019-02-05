import pandas as pd

def clean():
    # read in csv into dataframe
    df = pd.read_csv('malware_train.csv', low_memory=False)

    # clean up NaN values
    for column in df.columns:
        df[column] = df[column].fillna(0)

    file_name = 'malware_train_clean.csv'
    df.to_csv(file_name, encoding='utf-8')

clean()
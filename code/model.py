import pandas as pd 

def classification_model(df, folder, column_name, json_key):
    df.to_csv(f'datalake/refined/{folder}/data_full_{folder}_classified.csv')
    save_gbq(df, folder, 'classified_data', json_key)
    return df
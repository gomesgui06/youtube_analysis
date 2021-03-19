import pandas as pd 
import joblib


def classification_model(df, folder, column_name):
    
    classifier = joblib.load(f'datalake/model/{folder}/classifier.joblib')
    vectorizer = joblib.load(f'datalake/model/{folder}/vectorizer.joblib')

    df['label'] = classifier.predict(vectorizer.transform(df[column_name].values))
    
    df.to_csv(f'datalake/refined/{folder}/data_full_{folder}_classified.csv')
    return df
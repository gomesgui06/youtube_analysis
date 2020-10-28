import pandas as import pd
import numpy as np

def clean_function(df, column_text):
    df[f'{column_text}_cleaned'] =  df[[f'{column_text}']]\
            .replace(regex=r'[!/,.?-]',value='')\
            .apply(lambda x: x.astype(str).str.lower())\
            .apply(lambda x: x.astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
    
    return df 

def stop_words(df, column_name):
    # do something
    return df

def stemming(df, column_name):
    # do something
    return df

import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')


def clean_function(df, column_text):
    """
    Método que faz a limpeza do texto removendo pontos, virgulas, caracteres especiais e colocando o texto em minusculo

    Parametros: DataFrame, coluna para ser limpa

    Retorno: DataFrame com mais uma coluna_cleaned
    """
    df[f'{column_text}_cleaned'] =  df[[f'{column_text}']]\
            .replace(regex=r'[!/,.-]',value='')\
            .replace(to_replace=r"\b((?:k)+?|(?:l+o+)+l?|(?:h+a)+?|(?:h+e)+)\b", value='', regex=True)\
            .apply(lambda x: x.astype(str).str.lower())\
            .apply(lambda x: x.astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
    
    return df 

def stop_words_function(df, column_name, new_column_name):
    """
    Método que remove as stop_words
    Parametros: DataFrame, coluna para ser limpa, nome da nova coluna

    Retorno: DataFrame com mais uma coluna
    """
    
    stop_words = stopwords.words('portuguese')
    df[new_column_name] = df[column_name].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))

    return df

def tokenization (df,column_name, new_column_name):
    """
    Método que faz a tokenização, "quebra" o texto por palavra e transforma em lista
    Parametros: DataFrame, coluna para ser limpa, nome da nova coluna

    Retorno: DataFrame com mais uma coluna
    """

    df[new_column_name] = df[column_name].map(lambda x: word_tokenize(x))
    return df

def stemming(df, column_name, new_column_name):
    """
    Método que faz a stemização, volta para o radical
    Parametros: DataFrame, coluna para ser limpa, nome da nova coluna

    Retorno: DataFrame com mais uma coluna
    """
    snowball = SnowballStemmer(language = 'portuguese')
    df[new_column_name] = df[column_name].map(lambda x: [snowball.stem(y) for y in x])
    return df

def lematization (df, column_name, new_column_name):
    """
    Método que faz a lematização, transforma o tempo verbal
    Parametros: DataFrame, coluna para ser limpa, nome da nova coluna

    Retorno: DataFrame com mais uma coluna
    """
    lemmatizer = WordNetLemmatizer()
    df[new_column_name] = df[column_name].map(lambda x: [lemmatizer.lemmatize(y) for y in x])
    return df

def preprocessor (df, folder, column_name):
    """
    Método que faz todas as etapas de limpeza:
    1 - clean function
    2 - remove stop_words
    3 - tokenization
    4 - stemização
    5 - lematização
    Parametros: DataFrame, pasta, coluna para ser limpa

    Retorno: DataFrame com novas colunas (uma nova para cada etapa)
    """
    data = clean_function(df, column_name)
    data = stop_words_function(data, f'{column_name}_cleaned', f'{column_name}_stop_word')
    data = tokenization(data, f'{column_name}_stop_word', f'{column_name}_tokenized')
    data = stemming(data, f'{column_name}_tokenized', f'{column_name}_stemming')
    data = lematization(data, f'{column_name}_tokenized', f'{column_name}_lematized')
    data.to_csv(f'datalake/refined/{folder}/data_full_{folder}.csv')
    return data
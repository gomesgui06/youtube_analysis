import sys 
import os

import pandas as pd 
from configparser import RawConfigParser

from preprocessing import preprocessor
from youtube_crawler import processor_youtube_crawler
from database_save import save_gbq
from model import classification_model



config = RawConfigParser()
thisfolder = os.path.dirname(os.path.abspath( __file__ ))
initfile = os.path.join(thisfolder , 'config.cfg')
config.read(initfile)

# variaveis = sys.argv
json_key_name = config.get('bigquery' , 'bigquery_key_json_name')
json_key_path = config.get('bigquery' , 'bigquery_key_json_local_path')

def main():
    # channel_name = variaveis[1]
    # url_channel = variaveis[2]
    
    url_channel = 'https://www.youtube.com/c/LionBBQ/videos'
    channel_name = 'lion_bbq'

    json_key = f'{json_key_path}{json_key_name}'
    
    
    df_raw = processor_youtube_crawler(url_channel, channel_name)
    
    df_preprocessed = preprocessor(df_raw, channel_name, 'comment')
    
    df_classified = classification_model(df_preprocessed, 
                                         channel_name,
                                         'comment_lematized')
    
    
    save_gbq(df_classified, channel_name, 'classified_data', json_key)


if __name__ == '__main__':
    main()
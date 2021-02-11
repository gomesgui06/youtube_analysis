import pandas as pd 
import sys 
from preprocessing import preprocessor
from youtube_crawler import processor_youtube_crawler
from database_save import save_postgres


variaveis = sys.argv

def main():
    folder = variaveis[1]
    url_channel = variaveis[2]
    
    # url_channel = 'https://www.youtube.com/c/S%C3%93VIDE/videos'
    # folder = 'so_vide'
    
    # df = processor_youtube_crawler(url_channel, folder)
    # preprocessor(df, folder, 'comment')
    
    df = pd.read_csv(f'/home/gomes/estudo/youtube_analysis/datalake/refined/{folder}/data_full_so_vide_classified.csv')

    con = 'postgres://metabase:postgres@localhost:5432'
    save_postgres(df, con, folder, 'classified')

    
if __name__ == '__main__':
    main()
import pandas as pd 
import sys 
from preprocessing import preprocessor
from youtube_crawler import processor_youtube_crawler

variaveis = sys.argv

def main():
    folder = variaveis[1]
    url_channel = variaveis[2]
    
    # url_channel = 'https://www.youtube.com/c/S%C3%93VIDE/videos'
    # folder = 'so_vide'
    
    df = processor_youtube_crawler(url_channel, folder)
    preprocessor(df, folder, 'comment')
    
if __name__ == '__main__':
    main()
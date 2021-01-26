import pandas as pd  
from preprocessing import preprocessor
from youtube_crawler import processor_youtube_crawler

def main():
    url_channel = 'https://www.youtube.com/c/S%C3%93VIDE/videos'
    folder = 'so_vide'
    df = processor_youtube_crawler(url_channel, folder)
    preprocessor(df, folder, 'comment')
    
if __name__ == '__main__':
    main()
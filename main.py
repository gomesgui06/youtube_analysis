import pandas as pd  
from preprocessing import preprocessor
from youtube_crawler import youtube_crawler, get_url_video

def main():
    url_channel = 'https://www.youtube.com/c/S%C3%93VIDE/videos'
    folder = 'so_vide'
    youtube_crawler(url_channel, folder)
    
if __name__ == '__main__':
    main()
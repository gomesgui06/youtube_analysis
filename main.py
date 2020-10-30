import pandas as pd  
from preprocessing import preprocessor
from youtube_crawler import youtube_crawler


def main():
    column_text = 'comment'
    folder = 'lion_bbq'
    url_channel = 'https://www.youtube.com/c/LionBBQ/videos'
    # data = youtube_crawler(url_channel, folder)
    data = pd.read_csv(f'datalake/raw/{folder}/data_full_{folder}.csv')
    data = data[['video_title', 'comment', 'author']]    
    df = preprocessor(data, folder, column_text)


if __name__ == '__main__':
    main()
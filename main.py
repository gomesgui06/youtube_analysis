import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd  
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')


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
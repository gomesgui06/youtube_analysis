import pandas as pd  
from preprocessing import preprocessor
from youtube_crawler import youtube_crawler, get_url_video

import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    url_channel = 'https://www.youtube.com/c/S%C3%93VIDE/videos'
    youtube_crawler(url_channel, 'so_vide')
    # get_url_video(url_channel)
    
    
if __name__ == '__main__':
    main()
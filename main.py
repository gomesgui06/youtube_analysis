import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd 


def get_url_video(url_channel):
    urls = []
    video_titles = []

    with Chrome('/home/guilherme.gomes/chromedriver') as driver:
        wait = WebDriverWait(driver,50)
        driver.get(url_channel)

        for item in range(5): 
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
            time.sleep(15)


        for video_title in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#video-title"))):
            video_titles.append(video_title.text)
        
        for url in driver.find_elements_by_css_selector("#video-title"):
            urls.append(url.get_attribute('href'))
      
        
        df = pd.DataFrame(video_titles, columns=['video_title'])
        df['url'] = urls     

    return (df)

def get_video_comment(video):
    comments=[]
    # votes =[]
    # authors = []

    with Chrome('/home/guilherme.gomes/chromedriver') as driver:
        wait = WebDriverWait(driver,50)
        driver.get(video)

        for item in range(5): 
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
            time.sleep(15)

        for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text"))):
            comments.append(comment.text)
            print(comment.text)
        """
        for vote in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#vote-count-middle"))):
            votes.append(vote.text)
        
        for author in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#author-text"))):
            authors.append(author.text)
        """
        df = pd.DataFrame(comments, columns=['comment'])
        # df['comment'] = coments
        # df['vote'] = votes

    return df

def main():
    #url_channel = 'https://www.youtube.com/c/LionBBQ/videos'
    # url_channel = 'https://www.youtube.com/user/MrMatheusTor/videos'
    # video = 'https://www.youtube.com/watch?v=Qw_cU8fN8aU&ab_channel=MrMatheusTor'
    
    #df_youtube_videos = get_url_video(url_channel)
    df_youtube_videos = pd.read_csv('datalake/raw/youtube_videos.csv')
    youtube_video_list = df_youtube_videos.url.tolist()
    name_video_list = df_youtube_videos.video_title.tolist()

    count = 0 
    for youtube_video in youtube_video_list:
        
        print(f'vídeo: {youtube_video}')
        df_coments = get_video_comment(video=youtube_video)
        df_coments.to_csv(f'datalake/raw/coments_of_{name_video_list[count]}.csv')
        count = count+1    
    
    #df_youtube_videos.to_csv('datalake/raw/youtube_videos.csv')


if __name__ == '__main__':
    main()
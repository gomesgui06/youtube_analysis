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
    coments=[]
    # votes =[]
    authors = []

    with Chrome('/home/guilherme.gomes/chromedriver') as driver:
        wait = WebDriverWait(driver,50)
        driver.get(video)

        for item in range(10): 
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
            print(EC.visibility_of_element_located((By.TAG_NAME, "body")))
            print(wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END))
            time.sleep(15)

        for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text"))):
            coments.append(comment.text)
        """
        for vote in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#vote-count-middle"))):
            votes.append(vote.text)
        """
        for author in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#author-text"))):
            authors.append(author.text)
    
        df = pd.DataFrame(coments, columns=['comment'])
        df['author'] = authors

    return df

def main():
    # To Do
    # Passar a lista de vídeos e iterar pegando os comentários
    url_channel = 'https://www.youtube.com/user/MrMatheusTor/videos'
    # video = 'https://www.youtube.com/watch?v=Qw_cU8fN8aU&ab_channel=MrMatheusTor'
    
    df = get_url_video(url_channel)
    # df = get_video_comment(video=video)
    df.to_csv('teste.csv')


if __name__ == '__main__':
    main()
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd 

coments=[]
# votes =[]
authors = []

def get_video():
    with Chrome('/home/guilherme.gomes/chromedriver') as driver:
        wait = WebDriverWait(driver,50)
        video = 'https://www.youtube.com/watch?v=Qw_cU8fN8aU&ab_channel=MrMatheusTor'
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
        #print(df.head())
        #df.to_csv('comentarios.csv')

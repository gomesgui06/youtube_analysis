import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd 
from selenium import webdriver


def get_url_video(url_channel):
    urls = []
    video_titles = []

    with Chrome('/home/guilherme.gomes/chromedriver') as driver:
        wait = WebDriverWait(driver,50)
        driver.get(url_channel)

        for item in range(10): 
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
            time.sleep(15)


        for video_title in wait.until(EC.presence_of_all_elements_located((By.ID, "video-title"))):
            video_titles.append(video_title.text)
            print(f'Título do vídeo: {video_title.text}')
            
        
        for url in driver.find_elements_by_css_selector("#video-title"):
            urls.append(url.get_attribute('href'))
            print(f'URL: {url.get_attribute("href")}')      
        
        df = pd.DataFrame(video_titles, columns=['video_title'])
        df['url'] = urls   
          

    return (df)

def get_video_comment(video):
    comments=[]
    authors = []

    with Chrome('/home/guilherme.gomes/chromedriver') as driver:
        wait = WebDriverWait(driver,50)
        driver.get(video)

        count = 0 
        for item in range(15): 
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
            if count == 0:
                driver.execute_script("window.scrollTo(0, 400);")
                time.sleep(30)
            time.sleep(30)
            count= count+1
        
        
        for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content-text"))):
            comments.append(comment.text)
            print(f'Comentário: {comment.text}')

        
        for author in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#author-text"))):
            authors.append(author.text)
            print(f'Autor: {author.text}')


        
        df = pd.DataFrame(comments, columns=['comment'])
        df['author'] = authors


    return df

def video_list(df):
    
    videos_title = df.to_list()
    lista =[]

    for title in videos_title:
        lista.append(f'coments_of_{title}')
    
    return lista

def concat_df(lista):
    print('Função data_full')
    print(lista)
    print(type(lista))
    dfs = []

    for l in lista:
        dataframe = pd.read_csv(f'datalake/raw/lion_bbq/{l}.csv')
        dataframe['video_title'] = l
        dfs.append(dataframe)
    
    df = pd.concat(dfs, ignore_index=True)

    return df

def youtube_crawler(url_channel, folder):

    print(f'ETAPA 01 - Processando canal: {folder}')
    df_youtube_videos = get_url_video(url_channel)
    print(f'ETAPA 02 - Coletando vídeos do canal')
    print(f'Dataframe de vídeos: {df_youtube_videos.head()}')
    df_youtube_videos.to_csv(f'datalake/raw/{folder}/youtube_videos.csv', index=False)

    # df_youtube_videos = pd.read_csv(f'datalake/raw/{folder}/youtube_videos.csv')
    youtube_video_list = df_youtube_videos.url.tolist()
    name_video_list = df_youtube_videos.video_title.tolist()
    videos_processados = []

    count = 0 
    for youtube_video in youtube_video_list[:5]:
        
        print(f'{count} - vídeo: {youtube_video}')
        df_coments = get_video_comment(video=youtube_video)
        df_coments.to_csv(f'datalake/raw/{folder}/coments_of_{name_video_list[count]}.csv', index=False)
        count = count+1
        videos_processados.append(youtube_video)
        df_videos_processados = pd.DataFrame(videos_processados, columns=['videos_processados'])
        df_videos_processados.to_csv(f'datalake/raw/{folder}/videos_processados.csv', index=False)

    dataframe_youtube_video = pd.read_csv(f'datalake/raw/{folder}/youtube_videos.csv')
    lista = video_list(dataframe_youtube_video['video_title'])
    data = concat_df(lista)
    data.to_csv(f'datalake/raw/{folder}/data_full_{folder}.csv')
    return data


import os
import shutil
import sys
import pandas as pd

canal = sys.argv
canal = canal[1]

path_raw = f'datalake/raw/{canal}'
if not os.path.exists(path_raw):
    os.makedirs(path_raw)
    df = pd.DataFrame(columns=['video_title', 'url'])
    df.to_csv(f'datalake/raw/{canal}/videos_processados.csv')
else:
    shutil.rmtree(path_raw)           
    os.makedirs(path_raw)
    df = pd.DataFrame(columns=['video_title', 'url'])
    df.to_csv(f'datalake/raw/{canal}/videos_processados.csv')

path_refined = f'datalake/refined/{canal}'
if not os.path.exists(path_refined):
    os.makedirs(path_refined)
else:
    shutil.rmtree(path_refined)           
    os.makedirs(path_refined)

path_model = f'datalake/model/{canal}'
if not os.path.exists(path_model):
    os.makedirs(path_model)
else:
    shutil.rmtree(path_model)           
    os.makedirs(path_model)

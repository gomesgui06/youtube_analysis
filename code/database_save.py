from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas_gbq
from google.oauth2 import service_account
import pandas_gbq

def save_postgres(df, con, folder, nome_tabela):
    engine = create_engine(f'{con}/{folder}')
    print(f'NOME DA URL: {engine.url}')
    if not database_exists(engine.url):
        create_database(engine.url)

    print(database_exists(engine.url))
    df.to_sql(f'{folder}_{nome_tabela}', engine, if_exists='replace')

def save_gbq(df, folder, nome_tabela, path_json_key):

    credentials = service_account.Credentials.from_service_account_file(path_json_key)    
    # pandas_gbq.to_gbq(df, table_id, project_id=project_id)
    
    pandas_gbq.to_gbq(dataframe = df, 
                      destination_table = f'{folder}.{nome_tabela}', 
                      project_id = 'youtube-analise-307419', 
                      credentials = credentials,
                      if_exists = 'append')
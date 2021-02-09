from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

def save_postgres(df, con, folder, nome_tabela):
    # engine = create_engine(f'{con}/{folder}_{nome_tabela}')
    engine = create_engine(f'{con}/youtube_analytics')
    print(f'NOME DA URL: {engine.url}')
    if not database_exists(engine.url):
        create_database(engine.url)

    print(database_exists(engine.url))
    df.to_sql(f'{folder}_{nome_tabela}', engine, if_exists='replace')
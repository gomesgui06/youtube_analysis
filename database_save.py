from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

def save_postgres(df, con, save_postgres):
    engine = create_engine(f'{con}/{folder}')
    if not database_exists(engine.url):
        create_database(engine.url)

    print(database_exists(engine.url))
    df.to_sql(folder, engine)
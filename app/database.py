# import psycopg2
# from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from . config import settings

# SQLALCHEMY_DATABASE_URL = 'postgressql://<USERNAME>:<PASSWORD>@<IPADDRESS/HOSTNAME>/<DATABASENAME>'
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:root@localhost/fastapi'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='root', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('connected to DB!')
#         break
#     except Exception as error:
#         print('connection to DB failed!')
#         print('Error: ', error)
#         time.sleep(2)
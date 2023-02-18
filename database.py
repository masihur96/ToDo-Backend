from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker





engine= create_engine('postgresql://postgres:CFxgz3S3HOjVuwY5f2Rq@containers-us-west-111.railway.app:7958/railway',
                      echo=True)

Base = declarative_base()

Session = sessionmaker()
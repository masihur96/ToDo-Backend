from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker





engine= create_engine('postgresql://postgres:uT5NeW9H3Y5FmfNLUdEn@containers-us-west-59.railway.app:7397/railway',
                      echo=True)

Base = declarative_base()

Session = sessionmaker()
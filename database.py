from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker





engine= create_engine('postgresql://postgres:aweLD6S3XhMKtKyDMXj1@containers-us-west-121.railway.app:5889/railway',
                      echo=True)

Base = declarative_base()

def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()

Session = sessionmaker()
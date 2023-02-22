from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker





engine= create_engine('postgresql://postgres:L69v5j87V39YTVjeL1kI@containers-us-west-199.railway.app:6450/railway',
                      echo=True)

Base = declarative_base()

Session = sessionmaker()
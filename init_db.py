from database import engine,Base
from models import User,Task


Base.metadata.create_all(bind=engine)
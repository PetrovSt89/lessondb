from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://fwqofgkw:46_PaCBbTPQU-UMmbPzJDLjOil-XKz9A@mouse.db.elephantsql.com:5432/fwqofgkw')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
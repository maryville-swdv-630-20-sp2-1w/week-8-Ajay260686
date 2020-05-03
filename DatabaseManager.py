from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Items import Base


# Singleton Database Manager class for managing session
class DatabaseManager:
    engine = None
    base = None

    def ready(self):
        host = 'sqlite:///:memory:'
        if self.engine and self.base:
            return True
        else:
            try:
                self.engine = create_engine(host)
                self.base = declarative_base(bind=self.engine)
                Base.metadata.create_all(bind=self.engine)
                return True
            except:
                return False

    def getSession(self):
        if self.ready():
            Session = sessionmaker(bind=self.engine)
            session = Session()
            return session
        else:
            return None

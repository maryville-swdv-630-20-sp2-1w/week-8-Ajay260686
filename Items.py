from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

# The base class which our objects will be defined on.
Base = declarative_base()

# The CartInfo Table
class Items(Base):
    __tablename__ = 'items'

    # Every SQLAlchemy table should have a primary key named 'id'
    id = Column(Integer, Sequence('item_seq', metadata=Base.metadata), primary_key=True)
    name = Column(String)
    price = Column(Float)

    # Lets us print out a CartInfo object conveniently.
    def __repr__(self):
        return "<items(" \
               "id='%s', " \
               "name='%s'," \
               "price='%s')>" % (
                   self.id,
                   self.name,
                   self.price,
               )

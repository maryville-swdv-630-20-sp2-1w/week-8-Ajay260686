from sqlalchemy import *
from Items import Base

# The CartInfo Table
class Transactions(Base):
    __tablename__ = 'transactions'

    # Every SQLAlchemy table should have a primary key named 'id'
    id = Column(Integer, Sequence('tran_seq', metadata=Base.metadata), primary_key=True)
    customerFirstName = Column(String)
    customerLastName = Column(String)
    amount = Column(Float)
    accountNumber = Column(String)

    # Lets us print out a CartInfo object conveniently.
    def __repr__(self):
        return "<transactions(" \
               "id='%s', " \
               "customerFirstName='%s'," \
               "customerLastName='%s')," \
               "amount='%s'," \
               "accountNumber='%s')>" % (
                   self.id,
                   self.customerFirstName,
                   self.customerLastName,
                   self.amount,
                   self.accountNumber
               )

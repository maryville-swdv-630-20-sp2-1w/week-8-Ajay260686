from sqlalchemy.orm import sessionmaker
from Transactions import *


class PaymentsDAO:

    # Function to insert the object into database.
    def insertPayment(self, session, payments):
        session.add(payments)
        session.commit()
        print('Record in Table Transactions >>', payments.id)
        session.close()

    # Function to Query the object into database.
    def getPaymentByName(self, session,  queryValue):
        transactionByName = session.query(Transactions).filter(Transactions.name == queryValue).first()
        print(transactionByName)
        session.close()

    def getAllTransactions(self, session):
        transactions = session.query(Transactions).all()
        session.close()
        return transactions

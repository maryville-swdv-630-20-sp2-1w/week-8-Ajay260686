from abc import abstractmethod

from Payments import Payments


class Cash(Payments):

    def __init__(self, amount, accountNumber, customerFirstName, customerLastName):
        super().__init__(amount, accountNumber, customerFirstName, customerLastName)

    def payment(self):
        print('Processing Debit Card Transaction For the Amount::=>', self.amount,
              ' for the Account Number::=>', self.accountNumber,
              ' for the Customer', self.customerFirstName + ' ' + self.customerLastName)

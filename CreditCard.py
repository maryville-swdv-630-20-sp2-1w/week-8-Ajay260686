from abc import ABC

from Payments import Payments


class CreditCard(Payments):

    def __init__(self, amount, accountNumber, customerFirstName, customerLastName):
        super().__init__(amount, accountNumber, customerFirstName, customerLastName)

    def payment(self):
        print('Processing Credit Card Transaction of Amount::=>', self.amount,
              ' for the Account Number::=>',self.accountNumber,
              ' for the Customer', self.customerFirstName+' '+self.customerLastName)

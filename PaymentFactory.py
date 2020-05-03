from Cash import Cash
from Check import Check
from CreditCard import CreditCard
from DebitCard import DebitCard


class PaymentFactory:

    def __init__(self, tranType, amount, accountNumber, customerFirstName, customerLastName):
        self.tranType = tranType
        self.amount = amount
        self.accountNumber = accountNumber
        self.customerLastName = customerLastName
        self.customerFirstName = customerFirstName

    def processPayment(self):
        if self.tranType == "CREDIT":
            payments = CreditCard(self.amount, self.accountNumber, self.customerFirstName, self.customerLastName)
            payments.payment()
        elif self.tranType == "DEBIT":
            payments = DebitCard(self.amount, self.accountNumber, self.customerFirstName, self.customerLastName)
            payments.payment()
        elif self.tranType == "CHECK":
            payments = Check(self.amount, self.accountNumber, self.customerFirstName, self.customerLastName)
            payments.payment()
        else:
            payments = Cash(self.amount, self.accountNumber, self.customerFirstName, self.customerLastName)
            payments.payment()


if __name__ == "__main__":

    test = PaymentFactory('Credit', 10.00, '12345678', 'Ajay', 'Yadav')
    test1 = PaymentFactory('Debit', 50.00, '56789', 'Ansh', 'Yadav')
    test2 = PaymentFactory('Check', 90.00, '123343445678', 'Seema', 'Yadav')
    test.processPayment()
    test1.processPayment()
    test2.processPayment()


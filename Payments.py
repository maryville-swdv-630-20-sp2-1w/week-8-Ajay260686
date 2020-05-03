from abc import abstractmethod, ABC


class Payments(ABC):

    def __init__(self, amount, accountNumber, customerFirstName, customerLastName):
        self.amount = amount
        self.accountNumber = accountNumber
        self.customerLastName = customerLastName
        self.customerFirstName = customerFirstName

    @abstractmethod
    def payment(self):
        pass

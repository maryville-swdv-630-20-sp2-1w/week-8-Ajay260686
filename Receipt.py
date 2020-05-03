from abc import abstractmethod, ABC


class Receipt(ABC):

    def __init__(self, receiptType, paymentAmount, cartDictionary):
        self.receiptType = receiptType
        self.paymentAmount = paymentAmount
        self.cartDictionary = cartDictionary

    @abstractmethod
    def processReceipt(self):
        pass

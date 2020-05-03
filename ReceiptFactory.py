from ElectronicReceipt import ElectronicReceipt
from PaperReceipt import PaperReceipt


class ReceiptFactory:

    def __init__(self, receiptType, paymentAmount, cartDictionary):
        self.receiptType = receiptType
        self.paymentAmount = paymentAmount
        self.cartDictionary = cartDictionary

    def processReceipt(self):
        if self.receiptType == "PAPER":
            receipt = PaperReceipt(self.receiptType, self.paymentAmount, self.cartDictionary)
            receipt.processReceipt()
        else:
            self.receiptType == "ELECTRONIC"
            emailAddress = input('Enter consumers Email Address::')
            receipt = ElectronicReceipt(self.receiptType, self.paymentAmount, self.cartDictionary, emailAddress)
            receipt.processReceipt()

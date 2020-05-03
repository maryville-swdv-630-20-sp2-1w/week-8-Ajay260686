from Receipt import Receipt


class ElectronicReceipt(Receipt):

    def __init__(self, receiptType, paymentAmount, cartDictionary, emailAddress):
        super().__init__(receiptType, paymentAmount, cartDictionary)
        self.emailAddress = emailAddress

    def processReceipt(self):
        print('Email Sent to {email}'.format(email=self.emailAddress))

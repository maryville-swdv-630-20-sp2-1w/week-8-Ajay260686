from Receipt import Receipt


class PaperReceipt(Receipt):

    def __init__(self, receiptType, paymentAmount, cartDictionary):
        super().__init__(receiptType, paymentAmount, cartDictionary)

    def processReceipt(self):
        print('----------------------------------------------------------------')
        print('                    RECEIPT                            ')
        print('----------------------------------------------------------------')
        print('    Item Name   |    Unit Price   |   Quantity    |     Amount    ')
        print('----------------------------------------------------------------')
        receiptFormat = "{name:^17}{unitprice:^17}{qty:^17}{amount:^17}  "
        for k in range(self.cartDictionary.__len__()):
            print(receiptFormat.format(name=self.cartDictionary[k][0], unitprice=self.cartDictionary[k][1],
                                       qty=self.cartDictionary[k][2], amount=self.cartDictionary[k][3]))
        print('---------------------------------------------------------------')
        print('Total Amount Paid::$  %.2f' % self.paymentAmount)
        print('---------------------------------------------------------------')

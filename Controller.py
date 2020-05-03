from CartManager import CartManager
from ReceiptFactory import ReceiptFactory
from Utilities import entryScreenInput, showProductsAndReturnItemDictionary, scanOptions, \
    showCartInformation, processPurchase

print(' ------------------------------------')
print('| Welcome to XYZ Point Of Sale System|')
print(' ------------------------------------')
option = entryScreenInput()
if option:
    # Initializing the Core Object
    cart = CartManager()
    itemDictionary = {}
    cartDictionary = {}
    cartCounter = 0
    paymentAmount = 0
    status = False
    # Fetching List of Items from Database
    items = cart.returnAllAvailableItems()
    itemDictionary = showProductsAndReturnItemDictionary(items, itemDictionary)
    scanDecision = scanOptions('scan')
    if scanDecision:
        while True:
            itemId = eval(input('Enter Item ID ::'))
            itemQty = eval(input('Enter the Item Qty ::'))
            itemActualPrice = itemDictionary[itemId][1]
            itemName = itemDictionary[itemId][0]
            # Store Object in format Key: Item name, unit price, qty, total price
            cartDictionary[cartCounter] = itemName, itemActualPrice, itemQty, round(itemActualPrice * itemQty, 2)
            showCartInformation(cartDictionary)
            decision, value = scanOptions('add')
            if decision:
                cartCounter = cartCounter + 1
                continue
            else:
                # Payment Flow
                for k in range(cartDictionary.__len__()):
                    paymentAmount = round(paymentAmount + cartDictionary[k][3], 2)
                print('Total Payment Amount is :: %.2f' % paymentAmount)
                print('-----------------------------------------------------------------')
                print('Ready to proceed for Payment ...')
                print('-----------------------------------------------------------------')
                paymentDecision, value = scanOptions('pay')
                if paymentDecision:
                    status = processPurchase(cartDictionary)
                # Receipt Processing
                else:
                    print('Thanks for using XYZ POS')
                    break
                if status:
                    receipt, value = scanOptions('rpt')
                    if receipt:
                        receiptType, value = scanOptions('rpty')
                        if value == '1':
                            receipt = ReceiptFactory('PAPER', paymentAmount, cartDictionary)
                            receipt.processReceipt()
                        else:
                            receipt = ReceiptFactory('ELECTRONIC', paymentAmount, cartDictionary)
                            receipt.processReceipt()
                        break
                    else:
                        print('Thanks for using XYZ POS. Transaction Completed')
                        break
                else:
                    print('Thanks for using XYZ POS')
                    break

    else:
        print('Thanks for using XYZ POS. Transaction Completed')
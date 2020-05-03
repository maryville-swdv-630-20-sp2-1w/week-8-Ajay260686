from PaymentFactory import PaymentFactory


def entryScreenInput():
    print()
    print()
    print('*****************************************')
    print('Press Enter Key To Start Scanning Items')
    print('*****************************************')
    print()
    try:
        input()
        return True
    except SyntaxError:
        pass


def showProductsAndReturnItemDictionary(items, itemDictionary):
    productFormat = "{itemId:^20}{name:^20}{price:^20}  "
    print('----------------------------------------------------------------')
    print('                    Available Product List                      ')
    print('----------------------------------------------------------------')
    print('    Item Id        |        Item Name     |   Item Price        ')
    print('----------------------------------------------------------------')
    for result in items:
        print(productFormat.format(itemId=result.id, name=result.name, price=result.price))
        itemDictionary[result.id] = [result.name, result.price]
    print('----------------------------------------------------------------')
    return itemDictionary


def showCartInformation(cartDictionary):
    cartFormat = "{name:^20}{price:^22}{qty:^22}{amount:^17}"
    print(' ----------------------------------------------------------------------------')
    print('|                    Cart Information                                        |')
    print(' ----------------------------------------------------------------------------')
    print('|    Item Name     |        Unit Price     |    Qty        |      Amount     |')
    print(' ----------------------------------------------------------------------------')
    for result in cartDictionary:
        values = cartDictionary[result]
        print(cartFormat.format(name=values[0], price=values[1], qty=values[2],
                                amount=values[3]))

    print('----------------------------------------------------------------------------')


def scanOptions(option):
    status = False
    value = 0
    while True:
        if option == 'scan':
            scanDecision = input('Ready to Scan the Items. Please Enter Y for YES and N for NO :: ')
        elif option == 'add':
            scanDecision = input('Want to Add More Items...Press Y Otherwise Enter N ::')
        elif option == 'pay':
            scanDecision = input('Press Y to Enter the Payment Details and N to Cancel the Purchase :: ')
        elif option == 'rpt':
            scanDecision = input('Would Like to Generate a Receipt Yes(Y) or No(N) ? ::')
        elif option == 'rpty':
            scanDecision = input('Press 1 for Paper Receipt or 2 for Electronic Receipt :: ')
        try:
            if scanDecision.upper() in {'Y', 'N'}:
                if scanDecision.upper().__eq__('Y'):
                    status = True
                    break
                else:
                    status = False
                    break
            elif scanDecision in {'1', '2'} and option == "rpty":
                status = True
                value = scanDecision
                break
            else:
                raise ValueError
        except ValueError:
            print("---->Please Enter valid option<----------")
    return status, value


def getPaymentInformation():
    while True:
        mode = input(' Enter Payment Mode :: ')
        firstName = input(' Enter Customer First Name :: ')
        lastName = input(' Enter Customer Last Name :: ')
        try:
            modeVal = int(mode)
            firstVal = str(firstName)
            lastVal = str(lastName)
            break
        except ValueError:
            print("---->Please Enter Payment Details<----------")
    return mode, firstName, lastName


def processPurchase(cartDictionary, paymentAmount=0):
    # Payment Flow
    for k in range(cartDictionary.__len__()):
        paymentAmount = round(paymentAmount + cartDictionary[k][3], 2)
    print(' ----------------------------------------------------------------')
    print('| Total Payment Amount is :: $%.2f                               |'.format(paymentAmount))
    print(' ----------------------------------------------------------------')
    print('|                 Kindly Proceed for Payment                     |')
    print(' ----------------------------------------------------------------')
    print(' ----------------------------------------------------------------')
    print('|                 Payment Modes Available                        |')
    print(' ----------------------------------------------------------------')
    print(' Press 1 for Credit Card')
    print(' Press 2 for  Debit Card')
    print(' Press 3 for  Check Card')
    print(' Press 4 for  Cash')
    print(' Press 5 for  Cancel the Transaction')
    print('-----------------------------------------------------------------')
    mode, firstName, lastName = getPaymentInformation()
    if mode in {'1', '2', '3'}:
        accountNumber = input('Enter Account Number:: ')
        if mode == '1':
            transactionMode = 'CREDIT'
        elif mode == '2':
            transactionMode = 'DEBIT'
        else:
            transactionMode = 'CHECK'
            routingNumber = input('Enter Account Routing Number:: ')
        paymentFactory = PaymentFactory(transactionMode,
                                        paymentAmount,
                                        accountNumber,
                                        firstName,
                                        lastName)
        paymentFactory.processPayment()
        return True
    elif mode == '4':
        paymentFactory = PaymentFactory("CHECK",
                                        paymentAmount,
                                        "NA",
                                        firstName,
                                        lastName)
        paymentFactory.processPayment()
        return True
    else:
        return False


class Utilities:
    pass

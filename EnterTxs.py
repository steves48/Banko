#function to enter debit & create a transaction
import datetime, Presentation


#print(sorted(comp2Lst, key = lambda x: x[0]))#did not sort in place.  sorted on date



def CalculateBalance(LstTx):
    Balance = 0.0
    for transaction in LstTx:
        #The amount of each transaction is at index [6]
        Balance += transaction[6]
        #The balance at the end of each transaction is at the last index of each transaction list
        transaction[-1] = round(Balance,2)

def CalculateClearedBalance(LstTx):
    Balance = 0.0
    for transaction in LstTx:
        if transaction[7] == True:
            #print(transaction[6])
            Balance += transaction[6]
    return round(Balance,2)


def CustomDate():
    customDateInput = input("Enter the date as yyyy,mm,dd: ")
    yr = int(customDateInput[0:4])
    mo = int(customDateInput[5:7])
    day = int(customDateInput[-2:])
    return datetime.date(yr, mo, day)


def EnterDebit(ID):
    dateDecide = input("Hit 'enter' for today's date; 'd' for custom date; 'q' to quit entry: ")
    if dateDecide.lower() == "d":
        TheDate = CustomDate()
    elif dateDecide.lower() == "q":
        return
    else: TheDate = datetime.date.today()
    print(TheDate)
    #TheDate = DetermineDate()
    enterTransaction = input("Enter transaction as type or checkNo.,Description,Amount")
    enterCat = input("Enter the category & memo as 'category,memo")
    lstEnterTrans = enterTransaction.split(",")
    lstEnterCat = enterCat.split(",")
    type = lstEnterTrans[0]
    description = lstEnterTrans[1]
    amount = lstEnterTrans[2]
    # if not "." in amount:
    #     amount = amount + ".00"
    #     print("the amount:" , amount)
    # if amount[-2] == ".":
    #     amount = amount + "0"
    #     print("amount is:" , amount)
    # amount = float(amount)
    # amount = round(amount,2)
    category = lstEnterCat[0]
    memo = lstEnterCat[1]
    #Balance += amount
    #intUniqueId += 1
    eachTransaction = [ID, TheDate, type, description, category, memo, -float(amount), False, 0.0]
    print(eachTransaction)
    return eachTransaction


def EnterDeposit(ID):
    memoOption = None
    dateDecide = input("Hit 'enter' for today's date; 'd' for custom date; 'q' to quit entry: ")
    if dateDecide.lower() == "d":
        TheDate = CustomDate()
    elif dateDecide.lower() == "q":
        return
    else:
        TheDate = datetime.date.today()
    print(TheDate)
    enterTransaction = input("Enter amount of the deposit:")
    memoOption = input("Type in memo if desired; otherwise hit <enter>")
    if memoOption == None:
        memoOption = " "
    # lstEnterTrans = enterTransaction.split(",")
    # Description = lstEnterTrans[0]
    amount = enterTransaction
    eachTransaction = [ID,TheDate,"---","Deposit","",memoOption,float(amount),False,0.0]
    print(eachTransaction)
    return eachTransaction


def DesignateClearedTxs(TxLst):
    for trans in TxLst:
        if trans[7] == False:
            Presentation.PrintRegister([trans]) #must put trans in list for this function to work properly
            Decision = input("To mark transaction as cleared, hit 'c'; otherwise hit <enter>; hit 'q' to"
                             "return to main menu: ")
            if Decision.lower() == "c":
                trans[7] = True
            elif Decision.lower() == "q":
                print("Cleared balance review ended")
                return
            else:
                pass
    print("Cleared balance review complete")
    # ClearedBal = CalculateClearedBalance(TxLst)
    # print("Cleared balance is: ", ClearedBal)
    # return ClearedBal

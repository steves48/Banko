#Revisions

import EnterTxs, Presentation, StoreData


def ReviseTx(TxLst):
    IdExists = False
    DidChangeAmt = False
    DidChangeClearedStatus = False
    IdNum = int(input("Enter the unique ID of the transaction: "))
    #Find the transaction by its unique ID number
    for i in range(len(TxLst)):
        if TxLst[i][0] == IdNum:
            IdExists = True
            Location = i
            print("Transaction to revise: ")#, TxLst[Location])
            #Need to create a list within a list for the Presentation.PrintRegister function to work
            DLst = [TxLst[Location]]
            #Display the transaction to revise:
            Presentation.PrintRegister(DLst)
            break
    if IdExists == False:
        print("No such unique ID exists.")
        return

    print("""
    1 = Change date
    2 = Change type
    3 = Change description/payee
    4 = Change category
    5 = Change memo
    6 = change amount
    7 = change cleared status
    """)
    while True:
        changeItem = input("Enter the number of the item to revise.  Hit 'q' when finished: ")
        if changeItem == "1":
            Date = EnterTxs.CustomDate()
            TxLst[Location][1] = Date
        elif changeItem == "2":
            newType = input("Enter the type: ")
            TxLst[Location][2] = newType
        elif changeItem == "3":
            newDescrip = input("Enter the description: ")
            TxLst[Location][3] = newDescrip
        elif changeItem == "4":
            newCat = input("Enter the category: ")
            TxLst[Location][4] = newCat
        elif changeItem == "5":
            newMemo = input("Enter the memo: ")
            TxLst[Location][5] = newMemo
        elif changeItem == "6":
            newAmt = float(input("Enter the new amount: "))
            TxLst[Location][6] = newAmt
            DidChangeAmt = True
        elif changeItem == "7":
            TxLst[Location][7] = not TxLst[Location][7]
            DidChangeClearedStatus = True
        elif changeItem.lower() == "q":
            print("Revisions completed.")
            if DidChangeAmt == True:
                EnterTxs.CalculateBalance(TxLst)
                print("Revised balance = ", TxLst[-1][-1])
            if DidChangeClearedStatus == True:
                return True
            return False
        else: print("Invalid entry.")

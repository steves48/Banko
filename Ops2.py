"""
Bank3:  Check transaction record
Dev: SJSarewitz
12/28/2018


"""



import pickle, datetime, EnterTxs, Presentation, Revisions, Searches, StoreData

#data
startDate = None
endDate = None
lstByDate = []
objFile = None
Balance = None
intUniqueId = None
Triage = None
ClearedBal = None
ClearedBalLst = None
LstTrans = None
LstRecentTrans = None
RecordCB = None

#--------------------Processing________________________
#get data for balance, cleared balance and unique Id

objFile = open("Bankfile1.dat", "rb")
intUniqueId = pickle.load(objFile)  #Get the unique Id from file:  will be incremented by 1 for next transaction.
objFile.close()
#for cleared balance: get the list of the history of cleared balance calculations
objFile = open("ClearedBalanceRecord.dat", "rb")
ClearedBalLst = pickle.load(objFile)
ClearedBal = ClearedBalLst[-1][0] #this is the most recent cleared balance
objFile.close()

#for transaction record, get stored data:
LstTrans = StoreData.RetrieveTransLst()

#Each separate transaction is a list.  Balance is the last item in the list.
#  The last item of the last transaction in LstTrans is the final balance.
Balance = LstTrans[-1][-1]


print("Welcome to the checking account register\n")
print("Ending balance:" , Balance)
print("Today's balance:", Searches.GetTodaysBalance(LstTrans))
print("Cleared balance:", ClearedBal)
print("Last unique ID:", intUniqueId)
#Print the last 10 transactions on opening the script:
print("\nLast 10 transactions--------------------------------------------------")
LstRecentTrans = LstTrans[-10:]
Presentation.PrintRegister(LstRecentTrans)

#----------------I/O-------------------------------------------------------

while True:
    print("""
    MENU of options:
    Enter a debit......................w
    Enter a deposit....................d
    Print register for a date range....p
    Print complete register............c
    Search for text....................s
    Search for an amount...............a
    Check off cleared entries..........b
    Display cleared balance history....h
    Revise a transaction...............r
    Quit the program...................q or <enter>
    """)

    Triage = input("Type in your choice and hit <enter>\n ")
    if Triage.lower() == "w":
        #invoke function to enter the transactionq

        intUniqueId += 1
        EachTransaction = EnterTxs.EnterDebit(intUniqueId)
        #append the transaction to the list of transactions
        LstTrans.append(EachTransaction)
        StoreData.StoreAllTxs(LstTrans,intUniqueId)
        LstTrans = StoreData.RetrieveTransLst()
    elif Triage.lower() == "d":
        # invoke function to enter the transaction
        intUniqueId += 1
        EachTransaction = EnterTxs.EnterDeposit(intUniqueId)
        # append the transaction to the list of transactions
        LstTrans.append(EachTransaction)
    # invoke function to print transactions for a date range:
    elif Triage.lower() == "p":
        print("Start date...")
        startDate = EnterTxs.CustomDate()
        print("End date...")
        endDate = EnterTxs.CustomDate()
        for trans in LstTrans:
            if trans[1] >= startDate and trans[1] <= endDate:
                lstByDate.append(trans)
        Presentation.PrintRegister(lstByDate)
        #convert dates to mm/dd/yr format for print statement below
        strStartDate = Presentation.ConvertDate(startDate)
        strEndDate = Presentation.ConvertDate(endDate)
        print("--------------------------------------------------------------------------------------------------")
        print("End of register for date range", strStartDate, "to", strEndDate)
        print("--------------------------------------------------------------------------------------------------")
    elif Triage.lower() == "r":
        if Revisions.ReviseTx(LstTrans) == True: #This means the cleared status of a transaction was changed, so cleared
            #balance must be recalculated
            ClearedBal = EnterTxs.CalculateClearedBalance(LstTrans)
            print("Cleared balance after revision: ", ClearedBal)
            ClearedBalLst.append((ClearedBal,datetime.date.today()))
            StoreData.StoreClearedBalance(ClearedBalLst)
        StoreData.StoreAllTxs(LstTrans,intUniqueId)
    elif Triage.lower() == "s":
        Searches.SearchByText(LstTrans)
        # objFile = open("Transactions1.dat", "rb")
        # LstTrans = pickle.load(objFile) #LstTrans is the list of all recorded transactions
        # objFile.close()
    elif Triage.lower() == "a":
        Searches.SearchByAmount(LstTrans)
    elif Triage.lower() == "b":
        #To mark transactions as "cleared" and get the cleared balance
        EnterTxs.DesignateClearedTxs(LstTrans)
        NewClearedBal = EnterTxs.CalculateClearedBalance(LstTrans)
        print("New cleared balance equals: ", NewClearedBal)
        RecordCB = input("Do you wish to record the cleared balance (y/n) ?")
        if RecordCB.lower() == "y":
            ClearedBal = NewClearedBal
            ClearedBalLst.append((ClearedBal,datetime.date.today()))
            StoreData.StoreClearedBalance(ClearedBalLst)
            StoreData.StoreAllTxs(LstTrans,intUniqueId)
    elif Triage.lower() == "h":
        #Display the cleared balance history
        Presentation.DisplayClearedHx(ClearedBalLst)
    elif Triage.lower() == "c":
        #Display the entire register
        Presentation.PrintRegister(LstTrans)
        print("--------------------------------------------------")
    elif Triage.lower() == "q":
        break
    else: print("Invalid entry.  Try again.")

# #sort transactions by date
# LstTrans = EnterTxs.SortByDate(LstTrans)
# #compute balances at the date of eqach transaction.  Each transaction is a list.
# EnterTxs.CalculateBalance(LstTrans)

#print the entire transaction list
print("-----------------------Complete Register-----------------------------------------")
Presentation.PrintRegister(LstTrans)



# #pickle the final list of transactions, the last unique ID, and the cleared balance.  Note that the
#StoreAllTxs function isorts the tx's by date and calculates the balances prior to pickling the list of transactions.
StoreData.StoreAllTxs(LstTrans,intUniqueId)
StoreData.StoreClearedBalance(ClearedBalLst)
# objFile = open("Transactions1.dat", "wb")
# pickle.dump(LstTrans, objFile)
# objFile.close()
# #pickle the unique ID
# objFile = open("Bankfile1.dat", "wb")
# pickle.dump(intUniqueId,objFile)
# objFile.close()
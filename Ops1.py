#Ops1.py
"""
First draft, checkbook app
"""
import datetime, pickle, os, decimal
import EnterTxs
from decimal import Decimal


#variables
#eachTransaction = [uniqueId,date,type,Description,Amount,Balance,Cleared]
#lstTransactions = [[]]
#intUniqueId
Cleared = False
#Balance
#objFile = open pickle file
CurrentDate = datetime.date.today()
LstTrans = None

#processes




#i/o
#get data for balance and unique Id
#for unique Id, get initial data:
objFile = open("Bankfile1.dat", "rb")
intUniqueId = pickle.load(objFile)  #Get the unique Id from file:  will be incremented by 1 for next transaction.
objFile.close()
#for transaction record:
objFile = open("Transactions1.dat", "rb")#check to see if Transaction file contains any records
# if os.path.getsize("Transactions1.dat") == 0:
#      print("No transactions in file.")
#      objFile.close()
#      LstTrans = []
#      Balance = 0.0
# else:
LstTrans = pickle.load(objFile)
objFile.close()
Balance = LstTrans[-1][-1]
print("opening balance:" , Balance)

print("last unique ID:", intUniqueId)
print("Transaction list: ", LstTrans)



while True:
    txEntry = input("Type 't' to enter a transaction; otherwise hit any other key: ")
    if txEntry.lower() != "t":
        break
    else:
        dateDecide = input("Hit 'enter' for today's date; 'd' for custom date; 'q' to quit entry: ")
        if dateDecide.lower() == "d":
            customDateInput = input("Enter the date as yyyy,mm,dd: ")
            yr = int(customDateInput[0:4])
            mo = int(customDateInput[5:7])
            day = int(customDateInput[-2:])
            Date = datetime.date(yr,mo,day)
        elif dateDecide.lower() == "q":
            break
        else: Date = CurrentDate

        print(Date)
        enterTransaction = input("Enter transaction as type or checkNo.,Description,Amount")
        enterCat = input("Enter the category & memo as 'category,memo")
        lstEnterTrans = enterTransaction.split(",")
        lstEnterCat = enterCat.split(",")
        type = lstEnterTrans[0]
        description = lstEnterTrans[1]
        amount = float(lstEnterTrans[2])
        category = lstEnterCat[0]
        memo = lstEnterCat[1]
        Balance += amount
        intUniqueId += 1
        eachTransaction = [intUniqueId, Date, type, description, category, memo, float(amount), False, float(Balance)]
        print(eachTransaction)
        LstTrans.append(eachTransaction)
        print(LstTrans)




#save the new Id data:
objFile = open("Bankfile1.dat", "wb")
pickle.dump(intUniqueId,objFile)
objFile.close()

#for transactions:
if LstTrans != None and LstTrans != []:
    objFile = open("Transactions1.dat", "wb")
    pickle.dump(LstTrans,objFile)
    objFile.close()

print(LstTrans)

a = EnterTxs.SortByDate(LstTrans)
print("sorted: ", a)






# #get saved data for unique Id:
# objFile = open("Bankfile1.dat","rb+")
# if os.path.getsize("Bankfile1.dat") == 0:
#     intUniqueId = 0
# else:
#     intUniqueId = pickle.load(objFile)
#
# print("initial", intUniqueId)
# objFile.close()
#
# intUniqueId += 1 #test for pickling saving and accessing
#
# #save unique Id to pickle file:
# objFile = open("Bankfile1.dat", "wb")
# pickle.dump(intUniqueId, objFile)
# objFile.close()


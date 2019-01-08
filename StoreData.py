#StoreData

import pickle, EnterTxs

#Pickle the final list of transactions and unique ID:
def StoreAllTxs(TxLst,LastUniqueId):
    #first, sort all transactions by date; then calculate the balance at the end of each transaction
    TxLst = sorted(TxLst, key=lambda x: x[1])
    EnterTxs.CalculateBalance(TxLst)
    objFile = open("Transactions1.dat", "wb")
    pickle.dump(TxLst, objFile)
    objFile.close()
    #pickle the unique ID
    objFile = open("Bankfile1.dat", "wb")
    pickle.dump(LastUniqueId,objFile)
    objFile.close()

#Retrieve the list of transactions
def RetrieveTransLst():
    objFile = open("Transactions1.dat", "rb")
    LstTrans = pickle.load(objFile) #LstTrans is the list of all recorded transactions
    objFile.close()
    return LstTrans


#Store the cleared balance list
def StoreClearedBalance(ClearedBalanceLst):
    objFile = open("ClearedBalanceRecord.dat","wb")
    pickle.dump((ClearedBalanceLst),objFile)
    objFile.close()
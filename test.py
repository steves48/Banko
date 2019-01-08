#test

# import pickle
#
# objFile = open("Bankfile1.dat", "rb")
# print(pickle.load(objFile))
# objFile.close()

# import EnterTxs
# #
# # a = EnterTxs.EnterDebit(4,21.50)
# # print(a)
# b = [[1,2,3],[5,1,2]]
# a = EnterTxs.SortByDate(b)
# print(a)

a = 123
b = 456.78
c = 246.1
d = 8765.345678999

#from decimal import Decimal

# aD = Decimal(a)
# # print(aD)
# # print(Decimal(d))

# dR = round(d,2)
# print(dR)
# print(round(a,2))
#
# print(round(b,1))
#
# f = "abce"
# for char in f:
#     if char == ".":
#         print("Y")
# if not "." in f:
#     print("no")
import datetime, pickle, EnterTxs
# TheDate = datetime.date.today()
# print(TheDate)
# strDate = str(TheDate)
# print(strDate)
# mo = strDate[5:7]
# day = strDate[8:]
# yr = strDate[0:4]
# strDateUSForm = mo + "/" + day + "/" + yr
# print(strDateUSForm)


#cB = (0.0,TheDate)
# objFile = open("ClearedBalanceRecord.dat", "ab")
# pickle.dump(cB,objFile)
# objFile.close()

# tstLst = [(0.0,datetime.date.today())]
# objFile = open("ClearedBalanceRecord.dat", "wb")
# pickle.dump(tstLst,objFile)
# objFile.close()

# objFile = open("ClearedBalanceRecord.dat", "rb")
# out = pickle.load(objFile)
# print("cleared: ", out)
# objFile.close()
# print(out[0])

newLst = [[5,datetime.date.today(),"web","first descrip","first cat","first memo",45.56,False,0.0]]
objFile = open("Transactions1.dat","wb")
pickle.dump(newLst,objFile)
objFile.close()


objFile = open("Transactions1.dat", "rb")
LstTrans = pickle.load(objFile) #LstTrans is the list of all recorded transactions
objFile.close()
print(LstTrans)
# ans = EnterTxs.CalculateClearedBalance(LstTrans)
# print(ans)

def SortByDate(TransactionList):
    return sorted(TransactionList, key = lambda x: x[1])

tLst = [[55,datetime.date.today()], [107,datetime.date(2018,5,12)]]
a = SortByDate(tLst)
print(a)

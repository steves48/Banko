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



# objFile = open("ClearedBalanceRecord.dat", "rb")
# out = pickle.load(objFile)
# print("cleared: ", out)
# objFile.close()
# print(out[0])

# newLst = [[5,datetime.date.today(),"web","first descrip","first cat","first memo",45.56,False,0.0]]
# objFile = open("Transactions1.dat","wb")
# pickle.dump(newLst,objFile)
# objFile.close()
#
#
# objFile = open("Transactions1.dat", "rb")
# LstTrans = pickle.load(objFile) #LstTrans is the list of all recorded transactions
# objFile.close()
# print(LstTrans)
# # ans = EnterTxs.CalculateClearedBalance(LstTrans)
# # print(ans)
#
# def SortByDate(TransactionList):
#     return sorted(TransactionList, key = lambda x: x[1])
#
# tLst = [[55,datetime.date.today()], [107,datetime.date(2018,5,12)]]
# a = SortByDate(tLst)
# print(a)


# objFile = open("Test2.dat", "ab")
# pickle.dump("456", objFile)
# objFile.close()
#THIS IS IT
objFile = open("BackupTxs.dat","rb")
b = []
while True:
    try:
        c = pickle.load(objFile)
        b.append(c)
    except EOFError:
        break
objFile.close()
print("No. of records = ", len(b))
# for lst in b:
#     for tx in lst:
#         print(tx)

for i in range(len(b)):
    print("Record no. ", i)
    for tx in b[i]:#b[i][0] will be date; b[i][1] will be the tx list.  Need to overwrite backup file with the
        #new tx records that include the date in the tuple.
        print(tx)
    print("------------------")

#Need function to print selected tx record

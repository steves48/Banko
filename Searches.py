#Searches
import Presentation, datetime

def SearchByText(LstToSearch):
    strText = input("Enter the text you are seeking: ")
    strExact = input("For exact match, type 'e'; otherwise hit any key: ")
    LstResult = []
    Successful = False
    if strExact.lower() == "e":
        for trans in LstToSearch:
            if strText in trans:
                Successful = True
                LstResult.append(trans)
    else:
        for trans in LstToSearch:
            if strText.lower() in trans[2].lower() or strText.lower() in trans[3].lower()\
                    or strText.lower() in trans[4].lower() or strText.lower() in trans[5].lower():
                Successful = True
                LstResult.append(trans)
    if Successful == True:
        Presentation.PrintRegister(LstResult)
    else:
        print("No transactions match your search.")
    return

def GetTodaysBalance(LstToSearch):
    for i in range(len(LstToSearch)):
        if LstToSearch[i][1] > datetime.date.today():
            return LstToSearch[i-1][8]

def SearchByAmount(LstToSearch):
    fltAmount = float(input("Enter the amount you are seeking: "))
    LstResult = []
    Successful = False
    for trans in LstToSearch:
        if fltAmount == trans[6]:
            LstResult.append(trans)
            Successful = True
    if Successful == True:
        Presentation.PrintRegister(LstResult)
    else:
        print("No transactions match your search")
    return
#Presentation

#to create the right no. of spaces for printing:
def CreateSpace(spaces):
    remainderSpace = ""
    for i in range(spaces):
        remainderSpace += " "
    return remainderSpace

#find number of digits to left of decimal point in order to justify width by the decimal point itself
def DigitsToLeft(strNumber):
    intMantissaLen = len(strNumber) - 3  #no. of digits to left of decimal
    return intMantissaLen

#convert date format to US format mo/day/year
def ConvertDate(TheDate):
    strDate = str(TheDate)
    mo = strDate[5:7]
    day = strDate[8:]
    yr = strDate[0:4]
    strDateUSForm = mo + "/" + day + "/" + yr
    return strDateUSForm




#to format and print the transaction list (which is the check register)
def PrintRegister(Register):  #next 2 lines are a test print
    # for transaction in Register:
    #     print(transaction)
    print("UID   Date     " + " Type  " + "Description         " +  "Category             " + "Memo             " +  "Amount           " + "Balance        " + "Cleared")
    print("------------------------------------------------------------------------------------------------------------------------------")
    intLineCounter = 0
    spaceDate = "  "
    for trans in Register: #This inserts the no. of spaces between items in each tx, depending on how long previous item is, so items will match up with headings in columns...
        intLineCounter += 1
        strUId = str(trans[0]) #convert the unique ID to a string
        spaceUId = 5 - len(strUId) #insert the correct number of spaces after the unique id, depending on the no. of
        #characters in the id.
        remainderUId = CreateSpace(spaceUId)
        spaceType = 7 - len(trans[2])
        spaceDescrip = 20 - len(trans[3])
        spaceCat = 20 - len(trans[4])
        #see below for spaceMem...need to convert amount to string with 2 decimals
        balance = round(trans[8], 2) #convert balance to a string and add trailing 0 if necessary so there are 2 0's after decimal pt.
        strBalance = str(balance)
        if strBalance[-2] == ".":  #Add one zero to the end if only 1 digit to  right of decimal pt.
            strBalance = strBalance + "0"
        spaceAmt = 18 - len(strBalance) #no. of spaces in front of the balance depends on the no. of characters in balance
        spaceBal = 8
        remainderType = CreateSpace(spaceType)
        remainderDescript = CreateSpace(spaceDescrip)
        remainderCat = CreateSpace(spaceCat)
        #see below for remainderMem:  need to convert amount to string with 2 decimals
        remainderAmt = CreateSpace(spaceAmt)
        remainderBal = CreateSpace(spaceBal)
        amount = round(trans[6],2) #round the float to 2 decimals
        strAmount = str(amount)
        if strAmount[-2] == ".": #but if there was only one decimal, add a zero to the end
            strAmount = strAmount + "0"

        intAdjustment = DigitsToLeft(strAmount)  #Justify amount column to line up with decimals, depending on no.
        #of characters to left of decimal
        spaceMem = 20 - len(trans[5]) - intAdjustment #This adjusts for the no. of digits to left of decimal in transaction amount
        remainderMem = CreateSpace(spaceMem)
        #Convert the date to mm/dd/yr format
        strDate = ConvertDate(trans[1])
        print(str(trans[0]) + remainderUId + strDate + spaceDate + str(trans[2]) + remainderType + str(trans[3]) + remainderDescript + str(trans[4]) + remainderCat + str(
            trans[5]) + remainderMem + strAmount + remainderAmt + strBalance + remainderBal + str(trans[7]))
        if intLineCounter % 5 == 0:
            print("------------------------------------------------------------------------------------------------------------------------")

def DisplayClearedHx(ClrBalLst):
    print("Date           Cleared Balance\n------------------------------")
    for item in ClrBalLst:
        USDate = ConvertDate(item[1])
        print(USDate, "   ", item[0])
    print("------------------------------")
#Backup_Functions

import pickle, datetime, Presentation, EnterTxs

#store the backup file.  Each backup consists of a tuple of the unique ID[0], the date of the backup[1] and the transaction list[2].
def StoreBackupFile(TxLst):
    objFile = open("Id_Backup.dat","rb")#get the unique ID of the last backup, and increment it by 1
    BuId = int(pickle.load(objFile))
    objFile.close()
    BuId += 1
    print(BuId)
    TodaysDate = datetime.date.today()
    objFile = open("BackupTxs.dat", "ab")
    pickle.dump((BuId,TodaysDate, TxLst), objFile)
    objFile.close()
    objFile = open("LastBackupDate.dat", "wb")#store the date of the backup separately -- will be used to determine if
    #a backup should be done, when option is set to daily backup
    pickle.dump(TodaysDate, objFile)
    objFile.close()
    objFile = open("Id_Backup.dat", "wb") #store the unique ID of this backup
    pickle.dump(BuId,objFile)
    objFile.close()

def RetrieveBackupRegisters(BackupFile): #retrieve the backup file
    objFile = open(BackupFile,"rb")
    b = []
    #this routine loads all the pickled objects.  When the loop runs out of objects, it throws an error and
    #ends the loop. The list b will now include all the pickled objects.
    while True:
        try:
            c = pickle.load(objFile)
            b.append(c)
        except EOFError:
            break
    objFile.close()
    return b

def PrintBackupFile(bl): #used for printing multiple registers:  either the entire file of backups, or
    #backups by date.  The function does not work if only a single register is in the backup.
    print("This is the backup file requested.")
    print("-------------------------------------------------------------------------------------------------")
    #print("No. of records = ", len(bl))
    print("-------------------------------------------------------------------------------------------------")
    #Each bl[i] is a transaction list.  bl[i][0] is the unique ID,
    # bl[i][1] is the backup date and bl[i][2] is the transaction list  itself.
    for i in range(len(bl)):
        print("Record no. ", bl[i][0] , "Date: ", Presentation.ConvertDate(bl[i][1]))
        #for tx in bl[i][1]:#bl[i][1] will be date; bl[i][2] will be the tx list.
        Presentation.PrintRegister(bl[i][2])
        print("END of this register")
        print("##################################################################################################")

#Need function to print selected tx record
def BackupChoices():
    while True:
        print("""
        Menu of Backup Options:
        
        Print entire backup file...........................a
        Print most recent transaction list.................b
        Print a transaction list by ID number..............n
        Print transaction lists by date of the backup......d
        Set backup frequency...............................f
        Restore a backup register..........................r
        Quit the backup functions..........................q
        """)

#need to add:  options on frequency of backup; and a restore option

        Choice = input("Type in your choice and hit <enter>. ")
        CompleteBU = RetrieveBackupRegisters("BackupTxs.dat")
        if Choice.lower() == "a":
            print("\nNo. of records in the complete backup file = ", len(CompleteBU), "\n")
            PrintBackupFile(CompleteBU)
        elif Choice.lower() == "b":
            print("\nThis is the latest register backup:")
            print("----------------------------------------------------------")
            print("Backup ID:", CompleteBU[-1][0])
            print("Date of backup: ", Presentation.ConvertDate(CompleteBU[-1][1]))
            Presentation.PrintRegister(CompleteBU[-1][2])#print the latest register in the backup
        elif Choice.lower() == "n":
            #This prints the register with a specific unique ID number
            NumToPrint = int(input("Enter the ID number for the desired transaction list: "))
            for register in CompleteBU:
                if register[0] == NumToPrint:
                    print("\nBackup ID:", register[0])
                    print("Date of backup: ", Presentation.ConvertDate(register[1]))
                    Presentation.PrintRegister(register[2])
        elif Choice.lower() == "d":
            DateToRetrieve = EnterTxs.CustomDate()
            TheDate = Presentation.ConvertDate(DateToRetrieve)
            print("\nFor date " + TheDate + ":")
            BackupByDate = []
            for register in CompleteBU:
                if register[1] == DateToRetrieve:
                    BackupByDate.append(register)
            if len(register) == 1:
                Presentation.PrintRegister(register[2]) #for some reason, the PrintBackupFile function does not work if only 1
                #register is present, so this print function is used
            else:
                print("Number of records in the backup of this date: ", len(BackupByDate))
                PrintBackupFile(BackupByDate)
        elif Choice.lower() == "f":
            FrequencyBackupDecider()
        elif Choice.lower() == "r":
            IdToRestore = int(input("Enter the ID number of the backup register to restore: "))
            Confirm = input("Are you sure? This will permanently replace the current register by the backup (y/n)! ")
            if Confirm.lower() == "y":
                #if an invalid number was entered, an error message will print and the RestoreRegister function will not return "done".
                if RestoreRegister(IdToRestore,CompleteBU) == "done":
                    return "restored"

        elif Choice.lower() == "q":
            return

def FrequencyBackupDecider():
    CurrDecision = ObtainBackupFrequency()
    print("Currently, your backup frequency is set to", CurrDecision)
    Decision = input("To backup daily, enter 'daily'.\nTo backup whenever program quits, enter 'every'")
    textFile = open("BackupFreq.txt", "w")
    if Decision.lower() == "every":
        textFile.write("every")
    elif Decision.lower() == "daily":
        textFile.write("daily")
    else:
        print("Error:  invalid entry.")
    textFile.close()
    return

def ObtainBackupFrequency():
    textFile = open("BackupFreq.txt", "r")
    Decider = textFile.readline()
    textFile.close()
    return Decider

# def StoreDateOfBackup():
#     objFile = open("LastBackupDate.dat", "wb")
#     pickle.dump(datetime.date.today(), objFile)
#     objFile.close()

def ObtainDateOfLastBU():
    objFile = open("LastBackupDate.dat", "rb")
    LastDate = pickle.load(objFile)
    objFile.close()
    return LastDate

def RestoreRegister(IDToRestore, BUFile):
    for register in BUFile:
        if register[0] == IDToRestore:
            print("File found!!")
            objFile = open("Transactions1.dat", "wb")
            pickle.dump(register[2],objFile)
            objFile.close()
            print("Transaction list restored!")
            return "done"
    print("Invalid number entered.")
    return
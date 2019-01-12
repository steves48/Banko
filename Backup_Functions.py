#Backup_Functions

import pickle, datetime, Presentation, EnterTxs

#store the backup file.  Each backup consists of a tuple of the date of the backup and the transaction list.
def StoreBackupFile(TxLst):
    TodaysDate = datetime.date.today()
    objFile = open("BackupTxs.dat", "ab")
    pickle.dump((TodaysDate, TxLst), objFile)
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
    print("No. of records = ", len(bl))
    print("-------------------------------------------------------------------------------------------------")
    #Each bl[i] is a transaction list.  bl[i][0] is the backup date and bl[i][1] is the transaction list  itself.
    for i in range(len(bl)):
        print("Record no. ", i , "Date: ", Presentation.ConvertDate(bl[i][0]))
        #for tx in bl[i][1]:#bl[i][0] will be date; bl[i][1] will be the tx list.
        Presentation.PrintRegister(bl[i][1])
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
        Quit the backup functions..........................q
        """)

#need to add:  options on frequency of backup; and a restore option

        Choice = input("Type in your choice and hit <enter>. ")
        CompleteBU = RetrieveBackupRegisters("BackupTxs.dat")
        if Choice.lower() == "a":
            PrintBackupFile(CompleteBU)
        elif Choice.lower() == "b":
            Presentation.PrintRegister(CompleteBU[-1][1])#print the latest register in the backup
        elif Choice.lower() == "n":
            #This prints the register with the index number n (found by printing the entire backup file)
            NumToPrint = int(input("Enter the ID number for the desired transaction list: "))
            Presentation.PrintRegister(CompleteBU[NumToPrint][1])
        elif Choice.lower() == "d":
            DateToRetrieve = EnterTxs.CustomDate()
            TheDate = Presentation.ConvertDate(DateToRetrieve)
            print("For date " + TheDate + ":")
            BackupByDate = []
            for register in CompleteBU:
                if register[0] == DateToRetrieve:
                    BackupByDate.append(register)
            if len(register) == 1:
                Presentation.PrintRegister(register) #for some reason, the PrintBackupFile function does not work if only 1
                #register is present, so this print function is used
            else:
                PrintBackupFile(BackupByDate)
#now need to write function to select backup to print by 1, most recent; 2, by number
        elif Choice.lower() == "q":
            return
import csv
import codecs
from os import system
from time import sleep

quit = False

def readfile(file):
#    table = []
#    iteration = 0
    with open(file,"r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        headers = 'ID', 'TASK', 'CATEGORY', 'STATUS'
        print(f"{headers[0]:4} {headers[1]:20} {headers[2]:30} {headers[3]:20}", end="\n")
        print(f"_"*3, "_"*20, "_"*30, "_"*20, end="\n")
        for row in csvreader:
            print(f"{row['ID']:4} {row['TASK']:20} {row['CATEGORY']:30} {row['STATUS']:20}", end="\n")
    return


def addentry(file, task, category, status ):
    rowcounter = 0
    with open(file, "r") as csvfile:
        csvreader =csv.reader(csvfile)
        rowcount1 = len(list(csvreader))
        rowcount = rowcount1
    with open(file, "a+",newline="\n") as csvfile:
        csvreader = csv.DictReader(csvfile)
        csvwriter = csv.writer(csvfile)
        print(f"{rowcount}")
        csvwriter.writerow([rowcount, task, category, status])
    return


"""Main function"""
while not quit :
    system('cls')
    #print("Task Manager ", "\n")
    while True :
        print("Welcome to Task Manager ", "\n")
        choice = input("press (v) to view, press (a) to add, press (e) to edit, press (s) for statistics or press (x) to exit: ")
        system('cls')
        if choice.lower() == "v" :
            print("VIEW", "\n")
            readfile("taskfile.csv")
            continue
        elif choice.lower() == "a" :
            print ("ADD", "\n")        
            task = input("Enter TASK:")
            category = input("enter CATEGORY: ")
            status = input("enter STATUS: ")
            addentry("taskfile.csv", task, category, status)
            system("cls")
            readfile("taskfile.csv")
            print("\n"f"{task}, {category}, {status} entered into system")
            input("Record update sucesful. Press any key to continue ...")
            continue

        elif choice.lower() == "e" :
            print("EDIT")
            readfile("taskfile.csv")

            csvlist = list(csv.DictReader(open('taskfile.csv',"r")))                 
            choose = int(input("Choose: "))
            chosen =(csvlist[choose - 1]) # becuase its start with 0 to mitigate issue on rowcount(len)

            for row in csv.DictReader(open('taskfile.csv',"r")): # to print the header
                headers = 'ID', 'TASK', 'CATEGORY', 'STATUS'
                print(f"{headers[0]:4} {headers[1]:20} {headers[2]:30} {headers[3]:20}")
                print(f"{chosen['ID']:4} {chosen['TASK']:20} {chosen['CATEGORY']:30} {chosen['STATUS']:20}")
                break

            category_status = input("press (c) to change category or press (s) to change status: ") # choose what to edit category or status
            
            if category_status.lower() == "c" :
                chosen['CATEGORY'] = input("New CATEGORY: ")

#TODO: line 78 and 89 can be a function

                with codecs.open('taskfile.csv', "w", encoding='utf-8') as csvfile: # encoding added to remove line spaces # w is to rewrite all the content
                    fieldnames = ['ID', 'TASK', 'CATEGORY', 'STATUS'] # this will be rewrite
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # rewrite the csvfile
                    writer.writeheader()
                    for row in csvlist:
                        writer.writerow(row)
                input("Record update sucesful. Press any key to continue ...")

            elif category_status.lower() == "s" :
                chosen['STATUS'] = input("New STATUS: ")

                with codecs.open('taskfile.csv', "w", encoding='utf-8') as csvfile: # encoding added to remove line spaces # w is to rewrite all the content
                    fieldnames = ['ID', 'TASK', 'CATEGORY', 'STATUS'] # this will be rewrite
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # rewrite the csvfile
                    writer.writeheader()
                    for row in csvlist:
                        writer.writerow(row)
                input("Record update sucesful. Press any key to continue ...")

        elif choice.lower() == "s" :
            print("Statistics")
            readfile("taskfile.csv")
            csvlist = list(csv.reader(open('taskfile.csv',"r")))     
            statuscount = 0
      
            for status in csvlist:
                if 'pending' in status:
                    statuscount += 1

            with open('taskfile.csv', "r") as csvfile:
                csvreader =csv.reader(csvfile)
                rowcount1 = len(list(csvreader))
                rowcount = rowcount1 - 1
                #print(rowcount)
            
            statresult = (statuscount / rowcount) * 100
            completed = 100 - statresult

            print("***************** STATISTICS ********************")
            
            print(f"{statresult:.2f} % Pending")
            print(f"{completed:.2f} % Completed")
            input("Record Statistics. Press any key to continue ...")
            system("cls")
            continue

        elif choice.lower() == "x" :
            quit = True
            break
        else :
            print("Invalid input")
            sleep(1)
            continue

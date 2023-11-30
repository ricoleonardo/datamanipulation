import csv
from os import system

quit = False

def readfile(file):
    table = []
    iteration = 0
    with open(file,"r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(f"{row[0]:4} {row[1]:20} {row[2]:14} {row[3]:30} {row[4]: 20}", end="\n")
            if iteration == 0:
                print(f"_"*4, "_"*20, "_"*14, "_"*30, "_"*20, end="\n")
            iteration +=1
    return

print(readfile)

#def addentry(file, task,activity,category,status ):
    with open(file, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        csvwriter = csv.writer(csvfile)
        rowcount = len(list(csvreader))
        print(f"{rowcount}")
        csvwriter.writerow([rowcount, task, activity, category, status])
    return


#def modifyentry(file):
    
    

#while not quit:
#    system(cls)
#    print("Task Manager")





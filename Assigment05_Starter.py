# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Jonathan Ou, 5/8/2021, added code to complete assignment 5
# Jonathan Ou, 5/10/2021, added processing section to call up ToDoList.txt
# Jonathan Ou, 5/10/2021, added section to display current data
# Jonathan Ou, 5/10/2021, added section to add new time
# Jonathan Ou, 5/10/2021, added section to save data
# Jonathan Ou, 5/11/2021, added section to remove line from current data
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
objFile = None
strData = ""    # A row of text data from the file
dicRow = {}     # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []   # A list that acts as a 'table' of rows
strMenu = ""    # A menu of user options
strChoice = ""  # A Capture the user option selection
task = ""       # initial task callout prior to user input
priority = ""   # initial priority callout prior to user input
removeTask = "" # initial task to be removed callout prior to user input

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile,"r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task": lstRow[0],"Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("******* The current items TODO are *******")
        for row in lstTable: # iterates through the rows for all entries
            print(row["Task"]+"("+row["Priority"]+")")
        print("******************************************")
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task = input("What is the task? - ")
        priority = input("What is the priority? [high/low] - ")
        dicRow = {"Task": task,"Priority": priority.strip()}
        lstTable.append(dicRow) # adds new data to the end of the list currently stores
        print("Current Data in table:")
        for row in lstTable:
            print(row)
        print("******* The current items TODO are *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("******************************************")
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        removeTask = input("Which TASK would you like to remove? - ")
        for row in lstTable:
            if removeTask in row.values(): # checks of the task is in any of the values of the list
                lstTable.remove(row) # removes entire row in which value was flagged for removal
                print("The task has been removed.")
        print("******* The current items TODO are *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("******************************************")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        print("******* The current items TODO are *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("******************************************")
        save = input('Save this data to File? (y/n) - ')
        if (save == 'y'):
            objFile = open(strFile, 'w')
            for row in lstTable: # iterates throuhg the rows of the list
                objFile.write(row["Task"]+","+row["Priority"] + '\n')  # writes into text file the string based of keys
            print('Your data has been saved!')
            objFile.close()
        elif (save == 'n'):
            print('Your data was not saved.')
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program

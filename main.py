import os
import json
import datetime

if(os.path.exists("Accounts/") == False):
    os.mkdir("Accounts/")

account = int(input("Account Number: "))
exitstate = False

def getTime():
    return f"{datetime.datetime.now()}"

# If the account doesn't exist, make a new one
if(os.path.exists(f"Accounts/{account}.json") == False):
    newacc = input("Would you like to make a new account? (y/n): ")
    if(newacc.upper() == "Y"):
        name = input("Name: ")
        deposit = int(input("Deposit: "))
        dictionary = {
            "name": name,
            "balance": deposit,
            "last change": getTime()
        }
        json_object = json.dumps(dictionary, indent=4)
        with open(f"Accounts/{account}.json", "w") as outfile:
            outfile.write(json_object)
            outfile.close
    
        logfile = open("log.txt", "a")
        logfile.write(f"\n[{getTime()}] Account:{account} created")
        logfile.close

    exitstate = True

# Print out the account details
def read_Account():
    file = open(f"Accounts/{account}.json", "r")
    account_details = json.load(file)
    print(account_details)
    file.close

# Write new details    
def write_Account():
    file = open(f"Accounts/{account}.json", "r")
    account_details = json.load(file)
    file.close
    choice = input("What do you want to change? (n,b): ")
    
    #Change name
    if(choice.upper() == "N"):
        old_name = account_details["name"]
        print(old_name)
        new_name = input("New name: ")
        time = getTime()

        logfile = open("log.txt", "a")
        logfile.write(f"\n[{time}] Account:{account} name changed from {old_name} to {new_name}")
        logfile.close
        account_details["name"] = new_name
        account_details["last change"] = f"{time}"
        new_json = json.dumps(account_details, indent=4)

    #Change balance
    elif(choice.upper() == "B"):
        old_balance = account_details["balance"]
        print(old_balance)
        new_balance = int(input("New balance: "))
        time = getTime()

        logfile = open("log.txt", "a")
        logfile.write(f"\n[{time}] Account:{account} balanced changed from {old_balance} to {new_balance}")
        logfile.close
        account_details["balance"] = new_balance
        account_details["last change"] = f"{time}"
        new_json = json.dumps(account_details, indent=4)
    
    else:
        new_json = json.dumps(account_details, indent=4)

    #Writes to the JSON file
    with open(f"Accounts/{account}.json", "w") as outfile:
            outfile.write(new_json)
            outfile.close    
    
while True:
    if exitstate:
        break
    choice = input("What do you want to do? (r, w): ")
    if(choice.upper() == "R"):
        read_Account()
    elif(choice.upper() == "W"):
        write_Account()
    else:
        print("exiting")
        break
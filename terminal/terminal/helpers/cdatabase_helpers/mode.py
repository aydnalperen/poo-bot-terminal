from operator import ge
from models.mode_class import ModeClass
from ..ddatabase_helpers import *
from .create_helpers import *



def update_mode():
    print_modes()
    print("Which Mode Do You Want to Update?")
    answer = input("Enter the number of mode: ")

    modes = get_modes()
    updatedMode = modes[int(answer)-1]
    old_name = modes[int(answer)-1]["mode_name"]
    mode_name = input("Give a name to your updated mode and press ENTER: ")
    max_tax = float(input(
        "Write the maximum tax amount for updated mode and press ENTER: "))
    updatedMode["mode_name"] = mode_name
    updatedMode["max_tax"] = max_tax
    update_mode_by_id(updatedMode["id"],updatedMode)
    print("Mode is succesfully updated!")
    update_default_mode_by_name(old_name,updatedMode)
    print("Active mode is updated!")
def choose_mode():
    if not get_wallets():
        print("You have no wallets to create a mode, add a wallet first!")
        create_wallet()
    print("\nyour modes are: ")
    modes = get_modes()

    wallet_str = ""
    for i in range(len(modes)):
        for w in modes[i]["wallets"]:
            wallet_str += w["wallet_name"] + " "
        print("- "+str(i+1) + ". Name:" +
              modes[i]["mode_name"] + "  Wallets:" + wallet_str + " Max tax: " , modes[i]["max_tax"])

    indexes = input(
        "Write the numbers of modess that you want to use with your next trades (put spaces between numbers)")
    indexes.split()
    newModesArray = []
    old_default_modes = get_default_modes()
    for i in old_default_modes:
        delete_default_mode(i["id"])
    for i in indexes:
        try:
            newModesArray.append(modes[int(i) - 1])
            add_default_mode(modes[int(i) - 1])
        except:
            print("Invalid input!")
    
    # show what they have chosen
    print("Your new active modes are: ")
    wallet_str = ""

    for i in range(len(newModesArray)):
        for w in newModesArray[i]["wallets"]:
            wallet_str += w["wallet_name"] + " "
        print("- "+str(i+1) + ". Name:" +
              newModesArray[i]["mode_name"] + "  Wallets:" + wallet_str + " Max tax: " , newModesArray[i]["max_tax"])

    return newModesArray


def remove_mode():
    if not get_modes() :
        print("There is no saved mode!\n")
        print("Create a new one: \n")
        create_mode()
        return
    
    print_modes()
    modes = get_modes()
    default_modes = get_default_modes()
    print("Which Mode Do You Want to Delete?")
    answer = input("Enter the number of mode: ")
    
    default_mode_to_delete = get_default_mode_by_name(modes[int(answer)-1]["mode_name"])
    delete_default_mode(default_mode_to_delete[0]["id"])
    print("Mode ",modes[int(answer)-1]["mode_name"]," is removed from default modes." )
    delete_mode(modes[int(answer)-1]["id"])
    print("Mode ",modes[int(answer)-1]["mode_name"]," is succesfuly deleted.")
    
    if not get_default_modes():
        print("You have not a default (active) mode!")
        
        if not get_modes():
            print("You have no mode, create one!")
            create_mode()
        else:
            choose_mode()

def print_modes():
    print("Modes: ")
    modes = get_modes()
    walletString = ""
    for i in range(len(modes)):

        for w in modes[i]["wallets"]:
            walletString += w["wallet_name"] + " "
        print("- "+str(i+1) + ". Name:" +
              modes[i]["mode_name"] + "  Wallets:" + walletString + " Max tax: " , modes[i]["max_tax"])

from models.mode_class import ModeClass
from ..ddatabase_helpers import *
from .wallet import *

def create_mode():
    if(not get_wallets()):
        create_wallet()
    mode_name = input("Give a name to your new mode and press ENTER: ")

    print("Your wallets are:")

    wallets = get_wallets()
    for i in range(len(wallets)):
        print(str(i+1) + ". " + str(wallets[i]["wallet_name"]))

    wallets_to_add = map(int, input("Write the number of your wallets that you want to add this mode (put space between numbers): ").split())    
    final_wallets=[]
    for x in wallets_to_add: 
        final_wallets.append(wallets[x-1])

    max_tax = float(input(
        "Write the maximum tax amount for this mode and press ENTER: "))
    print("\n-> Added new ModeClass")
    print("ModeClass Name:", mode_name)
    for i in final_wallets:
        print("Wallets to buy:", i["wallet_name"],end=" ")

    print("Max tax amount:", max_tax)

    mode = ModeClass(mode_name, final_wallets, max_tax)
    mode.save_to_db()
    
    if len(get_modes())==1:
        add_default_mode(mode.__dict__)
        print("This mode is set as default since it is the only mode.")

    print("New mode added into database.")


def update_mode():
    print_modes()
    print("Which Mode Do You Want to Update?")
    answer = input("Enter the number of mode: ")

    modes = get_modes()
    updatedMode = modes[int(answer)-1]
    
    mode_name = input("Give a name to your updated mode and press ENTER: ")
    max_tax = float(input(
        "Write the maximum tax amount for updated mode and press ENTER: "))
    updatedMode["mode_name"] = mode_name
    updatedMode["max_tax"] = max_tax
    update_mode_by_id(updatedMode["id"],updatedMode)
    print("Mode is succesfully updated!")
def choose_mode():
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
        newModesArray.append(modes[int(i) - 1])
        add_default_mode(modes[int(i) - 1])
    
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
    
    print("Which Mode Do You Want to Delete?")
    answer = input("Enter the number of mode: ")
    delete_mode(modes[int(answer)-1]["id"])
    print("Mode ",modes[int(answer)-1]["mode_name"]," is succesfuly deleted.")

def print_modes():
    print("Modes: ")
    modes = get_modes()
    walletString = ""
    for i in range(len(modes)):

        for w in modes[i]["wallets"]:
            walletString += w["wallet_name"] + " "
        print("- "+str(i+1) + ". Name:" +
              modes[i]["mode_name"] + "  Wallets:" + walletString + " Max tax: " , modes[i]["max_tax"])

import models
import helpers

def update_mode():
    print_modes()
    print("Which Mode Do You Want to Update?")
    try:
        answer = input("Enter the number of mode: ")
        modes = helpers.get_modes()
        updatedMode = modes[int(answer)-1]
    except:
        print("Invalid Input!")
        return
    old_name = modes[int(answer)-1]["mode_name"]
    mode_name = input("Give a name to your updated mode and press ENTER: ")
    max_tax = float(input(
        "Write the maximum tax percentage for updated mode and press ENTER: "))
    updatedMode["mode_name"] = mode_name
    updatedMode["max_tax"] = max_tax
    helpers.update_mode_by_id(updatedMode["id"],updatedMode)
    print("Mode is succesfully updated!")
    helpers.update_default_mode_by_name(old_name,updatedMode)
    print("Active mode is updated!")
def choose_mode():
    if not helpers.get_wallets():
        print("You have no wallets to create a mode, add a wallet first!")
        helpers.create_wallet()
    print("\nyour modes are: ")
    modes = helpers.get_modes()

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
    old_default_modes = helpers.get_default_modes()
    for i in old_default_modes:
        helpers.delete_default_mode(i["id"])
    for i in indexes:
        try:
            newModesArray.append(modes[int(i) - 1])
            helpers.add_default_mode(modes[int(i) - 1])
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
    if not helpers.get_modes() :
        print("There is no saved mode!\n")
        print("Create a new one: \n")
        helpers.create_mode()
        return
    
    print_modes()
    modes = helpers.get_modes()
    default_modes = helpers.get_default_modes()
    try:
        print("Which Mode Do You Want to Delete?")
        answer = input("Enter the number of mode: ")    
        default_mode_to_delete = helpers.get_default_mode_by_name(modes[int(answer)-1]["mode_name"])
        
    except:
        print("Invalid Input!")
        return
    helpers.delete_default_mode(default_mode_to_delete[0]["id"])
    print("Mode ",modes[int(answer)-1]["mode_name"]," is removed from default modes." )
    helpers.delete_mode(modes[int(answer)-1]["id"])
    print("Mode ",modes[int(answer)-1]["mode_name"]," is succesfuly deleted.")
    
    if not helpers.get_default_modes():
        print("You have not a default (active) mode!")
        
        if not helpers.get_modes():
            print("You have no mode, create one!")
            helpers.create_mode()
        else:
            choose_mode()

def print_modes():
    print("Modes: ")
    modes = helpers.get_modes()
    walletString = ""
    for i in range(len(modes)):

        for w in modes[i]["wallets"]:
            walletString += w["wallet_name"] + " "
        print("- "+str(i+1) + ". Name:" +
              modes[i]["mode_name"] + "  Wallets:" + walletString + " Max tax: " , modes[i]["max_tax"])

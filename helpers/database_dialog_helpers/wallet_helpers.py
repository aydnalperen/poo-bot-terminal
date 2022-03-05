import models
import helpers

def update_wallet():
    print_wallets()
    print("Which Wallet Do You Want to Update?")
    answer = input("Enter the number of wallet: ")
    wallets = helpers.get_wallets()
    
    
    updatedWallet = wallets[int(answer)-1]

    try:
        buy_amount = float(input(
            "Give a buying amount to this wallet and press ENTER: "))
        gas_limit = int(input(
            "Give a gas limit to this wallet and press ENTER: "))
        buy_gwei = int(input(
            "Write the amount of buying gwei and press ENTER: "))
        sell_gwei = int(input(
            "Write the amount of selling gwei and press ENTER: "))
    except:
        print("Invalid Input! Enter a proper input!")
        return

    updatedWallet["buy_amount"] = buy_amount
    updatedWallet["gas_limit"] = gas_limit
    updatedWallet["buy_gwei"] = buy_gwei
    updatedWallet["sell_gwei"] = sell_gwei
    
    helpers.update_wallet_by_id(str(wallets[int(answer)-1]["id"]),updatedWallet)
    
    
    modes = helpers.get_modes()
    default_modes = helpers.get_default_modes()
    
    for mode in modes: 
        for wallet in mode["wallets"]:
            if wallet["wallet_name"] == updatedWallet["wallet_name"]:
                mode["wallets"].remove(wallet)
                wallet = updatedWallet
                mode["wallets"].append(wallet)
                helpers.update_mode_by_id(mode["id"],mode)
                print("Mode ",mode["mode_name"]," is updated due to changes in wallet ",wallet["wallet_name"]," .")
                break

    for mode in default_modes: 
        for wallet in mode["wallets"]:
            if wallet["wallet_name"] == updatedWallet["wallet_name"]:
                mode["wallets"].remove(wallet)
                wallet = updatedWallet
                mode["wallets"].append(wallet)
                helpers.update_default_mode_by_id(mode["id"],mode)
                print("Active Mode ",mode["mode_name"]," is updated due to changes in wallet ",wallet["wallet_name"]," .")
                break
            
    print("Wallet ",updatedWallet["wallet_name"]," is succesfully updated.")

    
def remove_wallet():
    
    print_wallets()
    wallets = helpers.get_wallets()
    print("Which Wallet Do You Want to Delete?")
    answer = input("Enter the number of wallet: ")
    
    modes = helpers.get_modes()
    
    modes_to_delete = []
    print("Modes ",end=" ")
    for mode in modes:
        for wallet in mode["wallets"]:
            if wallet["id"] == wallets[int(answer)-1]["id"]:
                modes_to_delete.append(mode)
                print(mode["mode_name"],end=" ")
                 
    print("will be deleted since they contain the wallet you want to remove.") 
    print("Do you want to continue?")
    print("1. Yes \n2. No")
    yes_no = input("Your Answer: ")
    if int(yes_no) == 1:
        for mode in modes_to_delete:
            helpers.delete_mode(mode["id"])
            print("Mode ",mode["mode_name"]," is deleted.")
            default_mode_to_delete = helpers.get_default_mode_by_name(mode["mode_name"])
            if default_mode_to_delete:
                helpers.delete_default_mode(default_mode_to_delete[0]["id"])       
    else:
        print("No wallet or mode is deleted.")
        return                    
    
    helpers.delete_wallet(wallets[int(answer)-1]["id"])
    print("Wallet ",wallets[int(answer)-1]["wallet_name"]," is succesfuly deleted.")

    if not helpers.get_default_modes():
        print("You have not a default (active) mode!")
        if not helpers.get_modes():
            print("You have no mode, create one!")
            helpers.create_mode()
        else:
            helpers.choose_mode()

def print_wallets():
    print("Wallets:")
    wallets = helpers.get_wallets()

    at_str = ""

    for i in range(len(wallets)):
        

        walletTemp = wallets[i]

        print("- "+str(i+1) + ". Name:" + walletTemp["wallet_name"] ,"Id:",walletTemp["id"], "  Adress:" + walletTemp["address"] + "  Buying Amount:" + str(walletTemp["buy_amount"]) + "  Buying Gwei:" + str(walletTemp["buy_gwei"])
              + "  Selling Gwei:" +str( walletTemp["sell_gwei"]) + "  Approved Tokens:" + at_str)

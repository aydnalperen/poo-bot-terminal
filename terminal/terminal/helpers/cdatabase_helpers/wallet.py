from models.wallet_class import WalletClass
from ..ddatabase_helpers import *
from ..transaction_helpers import *


def create_wallet():
    while True:
        name = input("Give a name to your wallet and press ENTER: ")
        address = input("Paste the wallet adress here and press ENTER: ")
        private_key = input("Write private key of your wallet and press ENTER: ")
        while True:
            try:
                buy_amount = float(input(
                "Give a buying amount to this wallet and press ENTER: "))
                break
            except:
                print("Please enter a number!")
                continue
        while True:
            try:
                gas_limit = float(input(
                "Give a gas limit to this wallet and press ENTER: "))
                break
            except:
                print("Please enter a number!")
                continue
        while True:
            try:
                buy_gwei = float(input(
                "Write the amount of buying gwei and press ENTER: "))
                break
            except:
                print("Please enter a number!")
                continue
        while True:
            try:
                sell_gwei = float(input(
                "Write the amount of selling gwei and press ENTER: "))
                break
            except:
                print("Please enter a number!")
                continue

        approved_tokens = []

        nonce = get_nonce(address)
        if nonce is None:
            print("Address you entered is invalid!")
            create_wallet()
            
            
            #return "wallet address problem"
        print("\n->Added your wallet.")

        print("WalletClass Name: "+name)
        print("WalletClass Adress: " + address)
        print("Buying Amonut: " + str(buy_amount))
        print("Gas Limit : " + str(gas_limit))
        print("Buying Gwei Limit" + str(buy_gwei))
        print("Selling Gwei Limit" + str(sell_gwei))

        wallet = WalletClass(name, address, private_key, buy_amount,
                            gas_limit, buy_gwei, sell_gwei, nonce, approved_tokens)
        wallet.save_to_db()

        print("New wallet added into database.")
        
        #
        print("Do you want to add another wallet?")
        options = ["1. Yes","2. No"]
        for a in options:
            print(a)
        answer = input("Enter 1 for 'Yes' and 2 for 'No': ")
        if int(answer) is not 1:
            break

def update_wallet():
    print_wallets()
    print("Which Wallet Do You Want to Update?")
    answer = input("Enter the number of wallet: ")
    wallets = get_wallets()
    
    
    updatedWallet = wallets[int(answer)-1]

    buy_amount = float(input(
            "Give a buying amount to this wallet and press ENTER: "))
    gas_limit = float(input(
        "Give a gas limit to this wallet and press ENTER: "))
    buy_gwei = float(input(
        "Write the amount of buying gwei and press ENTER: "))
    sell_gwei = float(input(
        "Write the amount of selling gwei and press ENTER: "))
    
    updatedWallet["buy_amount"] = buy_amount
    updatedWallet["gas_limit"] = gas_limit
    updatedWallet["buy_gwei"] = buy_gwei
    updatedWallet["sell_gwei"] = sell_gwei
    
    update_wallet_by_id(str(wallets[int(answer)-1]["id"]),updatedWallet)
    
    print("Wallet ",updatedWallet["wallet_name"]," is succesfully updated.")
def remove_wallet():
    
    print_wallets()
    wallets = get_wallets()
    print("Which Wallet Do You Want to Delete?")
    answer = input("Enter the number of wallet: ")
    
    modes = get_modes()
    
    for mode in modes:
        for wallet in mode["wallets"]:
            if wallet["id"] == wallets[int(answer)-1]["id"]:
                print("Mode ",mode["mode_name"]," will be deleted since it contains the wallet you want to delete.")
                print("Do you want to continue?")
                print("1. Yes \n2. No")
                yes_no = input("Your Answer: ")
                if int(yes_no) == 1:
                    delete_mode(mode["id"])
                    print("Mode ",mode["mode_name"]," is succesfuly deleted.")
                    continue
                elif int(yes_no)==2:
                    return                     
    delete_wallet(wallets[int(answer)-1]["id"])
    print("Wallet ",wallets[int(answer)-1]["wallet_name"]," is succesfuly deleted.")


def print_wallets():
    print("Wallets:")
    wallets = get_wallets()

    at_str = ""

    for i in range(len(wallets)):
        for at in wallets[i]["approved_tokens"]:
            at_str += at

        if(at_str == ""):
            at_str = "There is not approved token yet."

        walletTemp = wallets[i]

        print("- "+str(i+1) + ". Name:" + walletTemp["wallet_name"] ,"Id:",walletTemp["id"], "  Adress:" + walletTemp["address"] + "  Buying Amount:" + str(walletTemp["buy_amount"]) + "  Buying Gwei:" + str(walletTemp["buy_gwei"])
              + "  Selling Gwei:" +str( walletTemp["sell_gwei"]) + "  Approved Tokens:" + at_str)

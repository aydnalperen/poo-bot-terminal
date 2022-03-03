from models.wallet_class import WalletClass
from models.mode_class import ModeClass
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
                "Give a buying amount to this wallet and press ENTER (Default: 0.01): "))
                break
            except:
                print("Please enter a number!")
                continue
        while True:
            try:
                gas_limit = int(input(
                "Give a gas limit to this wallet and press ENTER (Default: 250000): "))
                break
            except:
                print("Please enter a number!")
                continue
        while True:
            try:
                buy_gwei = int(input(
                "Write the amount of buying gwei and press ENTER: "))
                break
            except:
                print("Please enter a number!")
                continue
        while True:
            try:
                sell_gwei = int(input(
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
        if int(answer) != 1:
            break

def create_mode():
    if(not get_wallets()):
        print("You have no wallet to create a mode, add a wallet first!")
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

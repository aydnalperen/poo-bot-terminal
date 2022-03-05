from models.wallet_class import WalletClass
from models.mode_class import ModeClass
from ..ddatabase_helpers import *
from ..transaction_helpers import *


def create_wallet():
    while True:
        name = input("Give a name to your wallet and press ENTER: ")
        address = input("Paste the wallet adress here and press ENTER: ")
        private_key = input("Write private key of your wallet and press ENTER: ")
        try:
            buy_amount = float(input(
            "Give a buying amount to this wallet and press ENTER (Default: 0.01): "))
            
        except:
            print("Buy amount is assigned to its default value 0.01! Enter a proper number to update it.")
            buy_amount = 0.01
        try:
            gas_limit = int(input(
            "Give a gas limit to this wallet and press ENTER (Default: 250000): "))
            
        except:
            print("Gas limit is assigned to its default value 250000! Enter a proper number to update it.")
            gas_limit = 25000
        try:
            buy_gwei = int(input(
            "Write the amount of buying gwei and press ENTER (Default: 5): "))
            
        except:
            print("Buy gwei is assigned to its default value 5! Enter a proper number to update it.")
            buy_gwei = 5
        try:
            sell_gwei = int(input(
            "Write the amount of selling gwei and press ENTER (Default: 5): "))
            
        except:
            print("Sell gwei is assigned to its default value 5! Enter a proper number to update it.")
            sell_gwei = 5

        approved_tokens = []

        nonce = get_nonce(address)
        if nonce is None:
            print("Address you entered is invalid!")
            create_wallet()
            
            
            #return "wallet address problem"
        print("\n->Added your wallet.")



        wallet = WalletClass(name, address, private_key,buy_amount  ,
                            gas_limit, buy_gwei, sell_gwei, nonce, approved_tokens)
        wallet.save_to_db()
        print("WalletClass Name: ",wallet.wallet_name)
        print("WalletClass Adress: " , wallet.address)
        print("Buying Amonut: " , wallet.buy_amount)
        print("Gas Limit : " , wallet.gas_limit)
        print("Buying Gwei Limit" , wallet.buy_gwei)
        print("Selling Gwei Limit"  ,wallet.sell_gwei)
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
    try:
        mode_name = input("Give a name to your new mode and press ENTER: ")
    except:
        print("There is no default name for modes, enter a valid name!")
        return

    print("Your wallets are:")

    wallets = get_wallets()
    for i in range(len(wallets)):
        print(str(i+1) + ". " + str(wallets[i]["wallet_name"]))

    while True:
        try:
            wallets_to_add = map(int, input("Write the number of your wallets that you want to add this mode (put space between numbers): ").split())    
            final_wallets=[]
            for x in wallets_to_add: 
                final_wallets.append(wallets[x-1])
            break
        except:
            print("Invalid Input!")    


    try:
        max_tax = float(input("Write the maximum tax amount for this mode and press ENTER: "))
    except:
        print("Invalid Input! Enter a number!")
        return
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


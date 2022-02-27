from .cdatabase_helpers import *

def entry_dialog():
    pass

def main_dialog():
    actions = ["1. Buy token", "2. Sell token", "3. Approve token","4. Modes and Wallets Options"
               ,"5. Show Modes and Wallets."]

    print("What action do you want to do?")
    for a in actions:
        print(a)
    answerIndex = input("Write number of your decision and press ENTER: ")
    return answerIndex

def network_dialog():
    network_options = [
        "1. BSC Testnet (PancakeSwap) (BSCTEST)", "2. BSC Mainnet (PancakeSwap) (BSC)"]

    print("Please choose a network")

    for o in network_options:
        print(o)

    network_selected = input("Write number of your decision and press ENTER: ")

    try:
        print("Connected Network:")
        print("-> " + network_options[int(network_selected)-1] + "\n")

        return network_options[int(network_selected)-1]
    except:
        print("Invalid Input!")
        network_dialog()

def modesAndWalletsOptionsDialog():
    modesAndWalletsOptions = ["1. Create Modes", "2. Add Wallet(s)","3. Choose Default Mode ","4. Delete a Wallet","5. Delete a Mode","6. Update a Wallet","7. Update a Mode"]
    
    print("What action do you want to do?")
    
    for a in modesAndWalletsOptions:
        print(a)
        
    answer = input("Write number of your decision and press ENTER: ")
    
    return answer

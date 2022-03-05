import helpers

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
    network_dict = {"network": network_selected}
    data = helpers.db.getDb(helpers.path.join(helpers.path.dirname(__file__)+"/.." + "/database/selected_network.json"))


    if not data.getAll():
        data.add(network_dict)  
    else:  
        network = data.getAll()
        data.updateById(network[0]["id"], network_dict)
    try:
        print("Connected Network:")
        print("-> " + network_options[int(network_selected)-1] + "\n")

        return network_options[int(network_selected)-1]
    except:
        print("Invalid Input!")
        network_dialog()

def modesAndWalletsOptionsDialog():
    modesAndWalletsOptions = ["1. Add Wallet(s)","2. Delete a Wallet","3. Update a Wallet","4. Create Modes","5. Choose Default Mode ","6. Delete a Mode","7. Update a Mode"]
    
    print("What action do you want to do?")
    
    for a in modesAndWalletsOptions:
        print("\n",a)
        
        
    answer = input("Write number of your decision and press ENTER: ")
    
    return answer

import helpers
def __main__():
    helpers.entry_dialog()

    network_index = helpers.network_dialog()

    if(not helpers.get_default_modes()):
        if not helpers.get_modes():
            print("You have no mode, create one first!")
            helpers.create_mode()
        else:
            print("You have no default mode, please chose one.")
            helpers.choose_mode()

    while(True):
        answer = int(helpers.main_dialog())

        if(answer == 1):
            helpers.buy_dialog()

        elif(answer == 2):
            helpers.sell_dialog()

        elif(answer == 3):
            helpers.approve_dialog()

        elif(answer == 4):
            secondOption = int(helpers.modesAndWalletsOptionsDialog())
            if(secondOption == 1):
                helpers.create_wallet()
            elif(secondOption == 2):
                helpers.remove_wallet()
            elif (secondOption == 3):
                helpers.wallet_helpers.update_wallet()    
            elif (secondOption == 4):
                helpers.create_mode()
            elif(secondOption == 5):
                helpers.choose_mode()
            elif (secondOption == 6):
                helpers.remove_mode()
            elif (secondOption == 7):
                helpers.mode_helpers.update_mode()
        elif(answer == 5):
            helpers.print_modes()
            helpers.print_wallets()

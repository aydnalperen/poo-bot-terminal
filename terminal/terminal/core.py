from helpers import *
from helpers.ddatabase_helpers import *

entry_dialog()

network_index = network_dialog()

if(not get_default_modes()):
    if not get_modes():
        print("You have no mode, create one first!")
        create_mode()
    print("You have no default mode, please chose one.")
    choose_mode()

while(True):
    answer = int(main_dialog())

    if(answer == 1):
        buy_dialog()

    elif(answer == 2):
        sell_dialog()

    elif(answer == 3):
        approve_dialog()

    elif(answer == 4):
        secondOption = int(modesAndWalletsOptionsDialog())
        if(secondOption == 1):
            create_mode()
        elif(secondOption == 2):
            create_wallet()
        elif(secondOption == 3):
            selected_modes = choose_mode()
        elif (secondOption == 4):
            remove_wallet()
        elif (secondOption == 5):
            remove_mode()
        elif (secondOption == 6):
            wallet.update_wallet()
        elif (secondOption == 7):
            mode.update_mode()
    elif(answer == 5):
        print_modes()
        print_wallets()

import helpers
import models

def buy_dialog():
    modes = helpers.get_default_modes()
    ca = input("BUY - Paste the contract address and press ENTER: ")
    trades=helpers.buy_token(modes, ca)
    isPending = True
    while isPending:
        helpers.print_current_trades(trades)
        for trade in trades:
            if not trade.status == "Pending":
                isPending = False
            else:
                isPending=True
                break
        helpers.sleep(2)

            

def approve_dialog():
    modes = helpers.get_default_modes()
    ca = input("APPROVE - Paste the contract address and press ENTER: ")
    helpers.approve_token(modes, ca)

def sell_dialog():
    modes = helpers.get_default_modes()
    ca = input("SELL - Paste the contract address and press ENTER: ")
    helpers.sell_token(modes, ca)
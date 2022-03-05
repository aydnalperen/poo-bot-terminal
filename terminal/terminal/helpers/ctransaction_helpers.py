from terminal.terminal.helpers.cdatabase_helpers.transactions import add_to_transactions, print_current_trades
from .cdatabase_helpers import *
from .transaction_helpers import *
import time
def buy_dialog():
    modes = get_default_modes()
    ca = input("BUY - Paste the contract address and press ENTER: ")
    trades=buy_token(modes, ca)
    
    while True:
        print_current_trades(trades)
        for trade in trades:
            if trade["status"] == "Pending":
                continue
        time.sleep(2)

            

def approve_dialog():
    modes = get_default_modes()
    ca = input("APPROVE - Paste the contract address and press ENTER: ")
    approve_token(modes, ca)

def sell_dialog():
    modes = get_default_modes()
    ca = input("SELL - Paste the contract address and press ENTER: ")
    sell_token(modes, ca)
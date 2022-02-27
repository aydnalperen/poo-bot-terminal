from .cdatabase_helpers import *
from .transaction_helpers import *

def buy_dialog(modes):
    ca = input("BUY - Paste the contract address and press ENTER: ")
    buy_token(modes, ca)

def approve_dialog(modes):
    ca = input("APPROVE - Paste the contract address and press ENTER: ")
    buy_token(modes, ca)

def sell_dialog(modes):
    ca = input("SELL - Paste the contract address and press ENTER: ")
    sell_token(modes, ca)